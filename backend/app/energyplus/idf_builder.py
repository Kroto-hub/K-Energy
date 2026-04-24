import os
import math
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__))
MONTH_DAY_COUNTS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def _normalize_month_day(month: int, day: int) -> tuple[int, int]:
    safe_month = max(1, min(12, int(month)))
    safe_day = max(1, min(MONTH_DAY_COUNTS[safe_month - 1], int(day)))
    return safe_month, safe_day


def _day_of_year(month: int, day: int) -> int:
    safe_month, safe_day = _normalize_month_day(month, day)
    return sum(MONTH_DAY_COUNTS[: safe_month - 1]) + safe_day


def _iter_calendar_days() -> list[tuple[int, int]]:
    days: list[tuple[int, int]] = []
    for month, day_count in enumerate(MONTH_DAY_COUNTS, start=1):
        for day in range(1, day_count + 1):
            days.append((month, day))
    return days


def _mark_active_range(mask: list[bool], start_month: int, start_day: int, end_month: int, end_day: int) -> None:
    start_doy = _day_of_year(start_month, start_day)
    end_doy = _day_of_year(end_month, end_day)
    if start_doy <= end_doy:
        for index in range(start_doy - 1, end_doy):
            mask[index] = True
        return
    for index in range(start_doy - 1, len(mask)):
        mask[index] = True
    for index in range(0, end_doy):
        mask[index] = True


def _build_hvac_schedule_compact(
    weekday_values: list[float],
    weekend_values: list[float],
    cooling_start_month: int,
    cooling_start_day: int,
    cooling_end_month: int,
    cooling_end_day: int,
    heating_start_month: int,
    heating_start_day: int,
    heating_end_month: int,
    heating_end_day: int,
) -> str:
    active_mask = [False] * sum(MONTH_DAY_COUNTS)
    _mark_active_range(active_mask, cooling_start_month, cooling_start_day, cooling_end_month, cooling_end_day)
    _mark_active_range(active_mask, heating_start_month, heating_start_day, heating_end_month, heating_end_day)
    calendar_days = _iter_calendar_days()

    segments: list[dict] = []
    current_active = active_mask[0]
    for index in range(1, len(active_mask)):
        if active_mask[index] == current_active:
            continue
        end_month, end_day = calendar_days[index - 1]
        segments.append({"end_month": end_month, "end_day": end_day, "active": current_active})
        current_active = active_mask[index]
    end_month, end_day = calendar_days[-1]
    segments.append({"end_month": end_month, "end_day": end_day, "active": current_active})

    off_values = [0.0] * 24
    lines = [
        "Schedule:Compact,",
        "    Sch_HVAC,",
        "    Fraction,",
    ]
    for segment_index, segment in enumerate(segments):
        lines.append(f"    Through: {segment['end_month']}/{segment['end_day']},")
        lines.append("    For: Weekdays,")
        current_weekday = weekday_values if segment["active"] else off_values
        current_weekend = weekend_values if segment["active"] else off_values
        for hour, value in enumerate(current_weekday, start=1):
            lines.append(f"    Until: {hour}:00, {value},")
        lines.append("    For: Weekends Holidays,")
        for hour, value in enumerate(current_weekend, start=1):
            suffix = ";" if segment_index == len(segments) - 1 and hour == 24 else ","
            lines.append(f"    Until: {hour}:00, {value}{suffix}")
    return "\n".join(lines)


def build_idf(
    area: float,
    floors: int,
    building_height: float,
    orientation: float,
    roof_u: float,
    wall_u: float,
    floor_u: float,
    window_u: float,
    window_shgc: float,
    wwr_south: float,
    wwr_north: float,
    wwr_east: float,
    wwr_west: float,
    occupancy_density: float,
    lighting_density: float,
    equipment_density: float,
    fresh_air_rate: float,
    infiltration_rate: float,
    summer_temp: float,
    winter_temp: float,
    cooling_start_month: int,
    cooling_start_day: int,
    cooling_end_month: int,
    cooling_end_day: int,
    heating_start_month: int,
    heating_start_day: int,
    heating_end_month: int,
    heating_end_day: int,
    labor_intensity: str,
    schedule_data: dict,
    output_path: str,
):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template('shoebox_template.idf')

    floor_area = area / floors
    width = math.sqrt(floor_area)
    length = width
    floor_height = building_height / floors
    volume = floor_area * floor_height

    activity_map = {
        "静坐": 120,
        "轻度劳动": 140,
        "中度劳动": 180,
        "重度劳动": 240,
    }
    activity_level = activity_map.get(labor_intensity, 120)

    regular_schedules = [
        {
            "name": "Sch_People",
            "weekday": schedule_data.get("people", {}).get("weekday", [0] * 24),
            "weekend": schedule_data.get("people", {}).get("weekend", [0] * 24),
        },
        {
            "name": "Sch_Lighting",
            "weekday": schedule_data.get("lighting", {}).get("weekday", [0] * 24),
            "weekend": schedule_data.get("lighting", {}).get("weekend", [0] * 24),
        },
        {
            "name": "Sch_Equipment",
            "weekday": schedule_data.get("equipment", {}).get("weekday", [0] * 24),
            "weekend": schedule_data.get("equipment", {}).get("weekend", [0] * 24),
        },
        {
            "name": "Sch_FreshAir",
            "weekday": schedule_data.get("fresh_air", {}).get("weekday", [1] * 24),
            "weekend": schedule_data.get("fresh_air", {}).get("weekend", [1] * 24),
        },
    ]
    hvac_schedule_compact = _build_hvac_schedule_compact(
        weekday_values=schedule_data.get("hvac", {}).get("weekday", [0] * 24),
        weekend_values=schedule_data.get("hvac", {}).get("weekend", [0] * 24),
        cooling_start_month=cooling_start_month,
        cooling_start_day=cooling_start_day,
        cooling_end_month=cooling_end_month,
        cooling_end_day=cooling_end_day,
        heating_start_month=heating_start_month,
        heating_start_day=heating_start_day,
        heating_end_month=heating_end_month,
        heating_end_day=heating_end_day,
    )

    fresh_air_s = fresh_air_rate / 3600.0
    fresh_air_design_flow = fresh_air_s * occupancy_density * area

    idf_content = template.render(
        area=area,
        floors=floors,
        building_height=building_height,
        floor_height=floor_height,
        width=width,
        length=length,
        volume=volume,
        multiplier=floors,
        orientation=orientation,
        roof_u=roof_u,
        wall_u=wall_u,
        floor_u=floor_u,
        window_u=window_u,
        window_shgc=window_shgc,
        wwr_south=wwr_south,
        wwr_north=wwr_north,
        wwr_east=wwr_east,
        wwr_west=wwr_west,
        occupancy_density=occupancy_density,
        lighting_density=lighting_density,
        equipment_density=equipment_density,
        fresh_air_rate=fresh_air_s,
        fresh_air_design_flow=fresh_air_design_flow,
        infiltration_rate=infiltration_rate,
        activity_level=activity_level,
        summer_temp=summer_temp,
        winter_temp=winter_temp,
        regular_schedules=regular_schedules,
        hvac_schedule_compact=hvac_schedule_compact,
    )

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(idf_content)

    return output_path
