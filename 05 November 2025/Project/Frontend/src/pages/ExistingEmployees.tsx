import { useEffect, useState } from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Briefcase, Target, RefreshCw } from "lucide-react";
import { getEmployees, getRecommendations } from "../api";

// 🧠 Type definitions for better type safety
interface Employee {
  id: number;
  name: string;
  email: string;
  skills: string[];
  past_projects?: string[];
}

interface Project {
  name: string;
  description: string;
  match: number;
}

const ExistingEmployees = () => {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [selectedEmployee, setSelectedEmployee] = useState<string>("");
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [loadingProjects, setLoadingProjects] = useState<boolean>(false);

  // Fetch employees when component loads
  useEffect(() => {
    async function fetchEmployees() {
      try {
        const data = await getEmployees();
        setEmployees(data);
      } catch (error) {
        console.error("Error fetching employees:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchEmployees();
  }, []);

  // Fetch project recommendations when employee changes
  useEffect(() => {
    async function fetchProjects() {
      if (!selectedEmployee) return;
      setLoadingProjects(true);
      try {
        const recs = await getRecommendations(selectedEmployee);
        setProjects(recs);
      } catch (error) {
        console.error("Error fetching recommendations:", error);
        setProjects([]);
      } finally {
        setLoadingProjects(false);
      }
    }
    fetchProjects();
  }, [selectedEmployee]);

  if (loading) return <p className="text-center mt-10">Loading employees...</p>;

  const employee = employees.find((e) => e.name === selectedEmployee);

  return (
    <div className="space-y-6 animate-fade-in">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold mb-2">Existing Employees</h1>
          <p className="text-muted-foreground">
            Select an employee to view their profile and recommendations
          </p>
        </div>
        <Button
          onClick={async () => {
            setLoading(true);
            const data = await getEmployees();
            setEmployees(data);
            setLoading(false);
          }}
          variant="outline"
          className="flex items-center gap-2"
        >
          <RefreshCw className="w-4 h-4" /> Refresh
        </Button>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Select Employee</CardTitle>
          <CardDescription>
            Choose from the list of registered employees
          </CardDescription>
        </CardHeader>
        <CardContent>
          <Select value={selectedEmployee} onValueChange={setSelectedEmployee}>
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Select an employee" />
            </SelectTrigger>
            <SelectContent>
              {employees.length === 0 ? (
                <SelectItem disabled value="none">
                  No employees found
                </SelectItem>
              ) : (
                employees.map((emp) => (
                  <SelectItem key={emp.id} value={emp.name}>
                    {emp.name}
                  </SelectItem>
                ))
              )}
            </SelectContent>
          </Select>
        </CardContent>
      </Card>

      {employee && (
        <div className="space-y-6 animate-scale-in">
          {/* Skills Card */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Briefcase className="w-5 h-5" />
                Skills
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="flex flex-wrap gap-2">
                {(employee.skills || []).map((skill, index) => (
                  <Badge
                    key={index}
                    variant="secondary"
                    className="text-sm py-1 px-3"
                  >
                    {skill}
                  </Badge>
                ))}
              </div>
            </CardContent>
          </Card>

          {/* Recommended Projects */}
          <div>
            <div className="flex items-center gap-2 mb-4">
              <Target className="w-6 h-6 text-primary" />
              <h2 className="text-2xl font-bold">Recommended Projects</h2>
            </div>

            {loadingProjects ? (
              <p>Loading project recommendations...</p>
            ) : projects.length === 0 ? (
              <p className="text-gray-500">
                No recommendations found for this employee.
              </p>
            ) : (
              <div className="grid md:grid-cols-2 gap-4">
                {projects.map((project, index) => (
                  <Card
                    key={index}
                    className="hover:shadow-lg transition-all duration-300 border-2 hover:border-primary"
                  >
                    <CardHeader>
                      <CardTitle className="text-xl">{project.name}</CardTitle>
                      <CardDescription>{project.description}</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-4">
                      <div className="flex items-center justify-between">
                        <span className="text-sm text-muted-foreground">
                          Skill Match
                        </span>
                        <Badge className="bg-primary text-primary-foreground">
                          {project.match}%
                        </Badge>
                      </div>
                      <Button className="w-full">Apply Now</Button>
                    </CardContent>
                  </Card>
                ))}
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default ExistingEmployees;