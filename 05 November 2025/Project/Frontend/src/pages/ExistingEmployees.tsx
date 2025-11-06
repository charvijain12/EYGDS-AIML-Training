import { useState, useEffect } from "react";
import { getEmployees, getRecommendations } from "../api";
import { Card, CardHeader, CardTitle, CardContent, CardDescription } from "@/components/ui/card";
import { Select, SelectTrigger, SelectContent, SelectItem, SelectValue } from "@/components/ui/select";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Briefcase, Target } from "lucide-react";

const ExistingEmployees = () => {
  const [employees, setEmployees] = useState<any[]>([]);
  const [selectedEmployee, setSelectedEmployee] = useState<string>("");
  const [projects, setProjects] = useState<any[]>([]);

  const fetchEmployees = async () => {
    const data = await getEmployees();
    setEmployees(data);
  };

  useEffect(() => {
    fetchEmployees();

    // 🔥 Refresh when new employee is added
    const handleEmployeeAdded = () => fetchEmployees();
    window.addEventListener("employeeAdded", handleEmployeeAdded);

    return () => {
      window.removeEventListener("employeeAdded", handleEmployeeAdded);
    };
  }, []);

  useEffect(() => {
    const fetchRecommendations = async () => {
      if (selectedEmployee) {
        const recs = await getRecommendations(selectedEmployee);
        setProjects(recs);
      } else {
        setProjects([]);
      }
    };
    fetchRecommendations();
  }, [selectedEmployee]);

  const employee = employees.find((e) => e.name === selectedEmployee);

  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-3xl font-bold mb-2">Existing Employees</h1>
        <p className="text-muted-foreground">
          Select an employee to view their profile and project recommendations
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Select Employee</CardTitle>
          <CardDescription>Choose from registered employees</CardDescription>
        </CardHeader>
        <CardContent>
          <Select value={selectedEmployee} onValueChange={setSelectedEmployee}>
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Select an employee" />
            </SelectTrigger>
            <SelectContent>
              {employees.map((emp) => (
                <SelectItem key={emp.id} value={emp.name}>
                  {emp.name}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </CardContent>
      </Card>

      {employee && (
        <div className="space-y-6 animate-scale-in">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Briefcase className="w-5 h-5" />
                Skills
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="flex flex-wrap gap-2">
                {employee.skills.map((skill: string, index: number) => (
                  <Badge key={index} variant="secondary" className="text-sm py-1 px-3">
                    {skill}
                  </Badge>
                ))}
              </div>
            </CardContent>
          </Card>

          <div>
            <div className="flex items-center gap-2 mb-4">
              <Target className="w-6 h-6 text-primary" />
              <h2 className="text-2xl font-bold">Recommended Projects</h2>
            </div>
            <div className="grid md:grid-cols-2 gap-4">
              {projects.map((project, index) => (
                <Card key={index} className="hover:shadow-lg transition-all duration-300 border-2 hover:border-primary">
                  <CardHeader>
                    <CardTitle className="text-xl">{project.name}</CardTitle>
                    <CardDescription>{project.description}</CardDescription>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-muted-foreground">Skill Match</span>
                      <Badge className="bg-primary text-primary-foreground">{project.match}%</Badge>
                    </div>
                    <Button className="w-full">Apply Now</Button>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ExistingEmployees;