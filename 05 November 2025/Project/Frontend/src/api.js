// src/api.js
export const API_URL = "http://127.0.0.1:8000";

export async function getEmployees() {
  const res = await fetch(`${API_URL}/api/employees`);
  return res.json();
}

export async function addEmployee(employee) {
  const res = await fetch(`${API_URL}/api/employees`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(employee)
  });
  return res.json();
}

export async function login(email, password) {
  const res = await fetch(`${API_URL}/api/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });
  return res.json();
}