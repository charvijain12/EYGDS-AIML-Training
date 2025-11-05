import { useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { AlertCircle, CheckCircle2 } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

const AddEmployee = () => {
  const { toast } = useToast();
  const [formData, setFormData] = useState({
    employeeId: "",
    fullName: "",
    email: "",
    skills: "",
  });
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setSuccess(false);

    // Basic validation
    if (!formData.employeeId || !formData.fullName || !formData.email || !formData.skills) {
      setError("All fields are required");
      return;
    }

    // Simulate checking if employee ID exists (replace with actual API call)
    const existingIds = ["12345", "67890"];
    if (existingIds.includes(formData.employeeId)) {
      setError("Employee ID already exists");
      return;
    }

    // Success
    setSuccess(true);
    toast({
      title: "Success!",
      description: "Employee added successfully",
    });
    
    // Reset form
    setTimeout(() => {
      setFormData({ employeeId: "", fullName: "", email: "", skills: "" });
      setSuccess(false);
    }, 2000);
  };

  return (
    <div className="max-w-2xl mx-auto animate-fade-in">
      <Card className="shadow-lg">
        <CardHeader>
          <CardTitle className="text-3xl">Add New Employee</CardTitle>
          <CardDescription>Register a new employee with their details and skills</CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-6">
            {error && (
              <Alert variant="destructive" className="animate-scale-in">
                <AlertCircle className="h-4 w-4" />
                <AlertDescription>{error}</AlertDescription>
              </Alert>
            )}

            {success && (
              <Alert className="border-green-500 text-green-700 bg-green-50 animate-scale-in">
                <CheckCircle2 className="h-4 w-4" />
                <AlertDescription>Employee added successfully!</AlertDescription>
              </Alert>
            )}

            <div className="space-y-2">
              <Label htmlFor="employeeId">Employee ID</Label>
              <Input
                id="employeeId"
                type="number"
                placeholder="Enter employee ID"
                value={formData.employeeId}
                onChange={(e) => setFormData({ ...formData, employeeId: e.target.value })}
                className="transition-all"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="fullName">Full Name</Label>
              <Input
                id="fullName"
                placeholder="Enter full name"
                value={formData.fullName}
                onChange={(e) => setFormData({ ...formData, fullName: e.target.value })}
                className="transition-all"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="email">Email</Label>
              <Input
                id="email"
                type="email"
                placeholder="Enter email address"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                className="transition-all"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="skills">Skills</Label>
              <Input
                id="skills"
                placeholder="Enter skills (comma separated)"
                value={formData.skills}
                onChange={(e) => setFormData({ ...formData, skills: e.target.value })}
                className="transition-all"
              />
              <p className="text-sm text-muted-foreground">Example: React, Python, Machine Learning</p>
            </div>

            <Button type="submit" className="w-full">
              Add Employee
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
};

export default AddEmployee;
