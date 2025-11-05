import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Users, UserPlus } from "lucide-react";

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="max-w-4xl mx-auto space-y-8 animate-fade-in">
      <div className="text-center space-y-4">
        <h1 className="text-4xl font-bold text-foreground">
          Welcome to ProjectMate
        </h1>
        <p className="text-xl text-muted-foreground">
          Your personal internal growth companion
        </p>
      </div>

      <div className="grid md:grid-cols-2 gap-6 mt-12">
        <Card className="p-8 hover:shadow-lg transition-all duration-300 cursor-pointer group border-2 hover:border-primary"
          onClick={() => navigate("/employees")}>
          <div className="flex flex-col items-center text-center space-y-4">
            <div className="w-20 h-20 rounded-full bg-primary/10 flex items-center justify-center group-hover:bg-primary/20 transition-colors">
              <Users className="w-10 h-10 text-primary" />
            </div>
            <h2 className="text-2xl font-semibold">Existing Employee</h2>
            <p className="text-muted-foreground">
              View profiles, skills, and get project recommendations
            </p>
            <Button className="w-full mt-4">View Employees</Button>
          </div>
        </Card>

        <Card className="p-8 hover:shadow-lg transition-all duration-300 cursor-pointer group border-2 hover:border-secondary"
          onClick={() => navigate("/add-employee")}>
          <div className="flex flex-col items-center text-center space-y-4">
            <div className="w-20 h-20 rounded-full bg-secondary/10 flex items-center justify-center group-hover:bg-secondary/20 transition-colors">
              <UserPlus className="w-10 h-10 text-secondary" />
            </div>
            <h2 className="text-2xl font-semibold">Add New Employee</h2>
            <p className="text-muted-foreground">
              Register a new employee with their skills and details
            </p>
            <Button className="w-full mt-4" variant="secondary">Add Employee</Button>
          </div>
        </Card>
      </div>
    </div>
  );
};

export default Home;
