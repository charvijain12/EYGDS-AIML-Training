// src/api.ts

// --- Type definitions ---
export interface Employee {
  id: number;
  name: string;
  email: string;
  skills: string[];
  past_projects?: string[];
}

export interface Project {
  name: string;
  description: string;
  match: number;
}

// --- API Base URL ---
const BASE_URL = "http://127.0.0.1:8000/api";

// --- Get all employees ---
export async function getEmployees(): Promise<Employee[]> {
  try {
    const res = await fetch(`${BASE_URL}/employees`);
    if (!res.ok) {
      throw new Error(`Failed to fetch employees: ${res.statusText}`);
    }
    return await res.json();
  } catch (error) {
    console.error("Error fetching employees:", error);
    return [];
  }
}

// --- Get project recommendations for a specific employee ---
export async function getRecommendations(employeeName: string): Promise<Project[]> {
  try {
    const res = await fetch(`${BASE_URL}/recommend/${employeeName}`);
    if (!res.ok) {
      throw new Error(`Failed to fetch recommendations: ${res.statusText}`);
    }
    return await res.json();
  } catch (error) {
    console.error("Error fetching recommendations:", error);
    return [];
  }
}

// --- Add a new employee (used in AddEmployee.tsx) ---
export async function addEmployee(employeeData: {
  name: string;
  email: string;
  skills: string[];
  past_projects?: string[];
}): Promise<{ message: string; id?: number }> {
  try {
    const res = await fetch(`${BASE_URL}/employees`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(employeeData),
    });

    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.detail || "Failed to add employee");
    }

    return await res.json();
  } catch (error) {
    console.error("Error adding employee:", error);
    return { message: "Failed to add employee" };
  }
}