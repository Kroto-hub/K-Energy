import client from "./client";

export const healthCheck = () => client.get("/health");
