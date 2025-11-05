import { useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Briefcase, Target } from "lucide-react";

// Mock data (replace with API calls)
const employees = [
  { id: "1", name: "Alice Johnson", skills: ["React", "TypeScript", "Node.js"] },
  { id: "2", name: "Bob Smith", skills: ["Python", "Machine Learning", "TensorFlow"] },
  { id: "3", name: "Carol Williams", skills: ["Java", "Spring Boot", "AWS"] },
];

const mockProjects = {
  "Alice Johnson": [
    { name: "E-commerce Platform", description: "Build a scalable shopping platform", match: 95 },
    { name: "Admin Dashboard", description: "Create internal analytics dashboard", match: 87 },
  ],
  "Bob Smith": [
    { name: "ML Pipeline", description: "Data processing and model training", match: 92 },
    { name: "Recommendation Engine", description: "User behavior prediction system", match: 89 },
  ],
  "Carol Williams": [
    { name: "Cloud Migration", description: "Move legacy apps to AWS", match: 91 },
    { name: "Microservices API", description: "Build REST APIs with Spring", match: 88 },
  ],
};

const ExistingEmployees = () => {
  const [selectedEmployee, setSelectedEmployee] = useState<string>("");
  const employee = employees.find((e) => e.name === selectedEmployee);
  const projects = selectedEmployee ? mockProjects[selectedEmployee as keyof typeof mockProjects] || [] : [];

  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-3xl font-bold mb-2">Existing Employees</h1>
        <p className="text-muted-foreground">Select an employee to view their profile and recommendations</p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Select Employee</CardTitle>
          <CardDescription>Choose from the list of registered employees</CardDescription>
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
                {employee.skills.map((skill, index) => (
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
