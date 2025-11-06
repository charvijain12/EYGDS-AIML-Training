import { useState } from "react";
import { addEmployee } from "../api";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { toast } from "@/components/ui/use-toast";

interface EmployeeForm {
  name: string;
  email: string;
  skills: string;
  past_projects: string;
}

const AddEmployee = () => {
  const [form, setForm] = useState<EmployeeForm>({
    name: "",
    email: "",
    skills: "",
    past_projects: "",
  });
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = async () => {
    if (!form.name || !form.email) {
      toast({ title: "Error", description: "Name and email are required", variant: "destructive" });
      return;
    }

    setLoading(true);
    const employeeData = {
      name: form.name,
      email: form.email,
      skills: form.skills.split(",").map((s) => s.trim()),
      past_projects: form.past_projects
        ? form.past_projects.split(",").map((p) => p.trim())
        : [],
    };

    const response = await addEmployee(employeeData);
    setLoading(false);

    if (response.message.includes("success")) {
      toast({ title: "Success", description: "Employee added successfully ✅" });
      setForm({ name: "", email: "", skills: "", past_projects: "" });

      // 🔥 Trigger a refetch event (Custom event)
      window.dispatchEvent(new Event("employeeAdded"));
    } else {
      toast({ title: "Error", description: response.message, variant: "destructive" });
    }
  };

  return (
    <div className="space-y-6">
      <Card>
        <CardHeader>
          <CardTitle>Add New Employee</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <Input name="name" value={form.name} onChange={handleChange} placeholder="Full Name" />
          <Input name="email" value={form.email} onChange={handleChange} placeholder="Email" />
          <Input name="skills" value={form.skills} onChange={handleChange} placeholder="Skills (comma-separated)" />
          <Input
            name="past_projects"
            value={form.past_projects}
            onChange={handleChange}
            placeholder="Past Projects (optional)"
          />
          <Button onClick={handleSubmit} disabled={loading} className="w-full">
            {loading ? "Adding..." : "Add Employee"}
          </Button>
        </CardContent>
      </Card>
    </div>
  );
};

export default AddEmployee;