import api from "../api/api";

export const login = async (username, password) => {
    const response = await api.post("/auth/login", {
        username,
        password
    });

    return response.data;
};

export const register = async (user) => {
    const response = await api.post("/auth/register", user);
    return response.data;
};