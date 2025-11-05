import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { TrendingUp, ExternalLink, Zap } from "lucide-react";

const trendingSkills = [
  {
    name: "MLOps",
    trend: "+45%",
    resources: [
      { title: "MLOps Tutorial", url: "https://www.geeksforgeeks.org/machine-learning/mlops-everything-you-need-to-know/" },
      { title: "Coursera Course", url: "https://www.coursera.org/courses?query=mlops&msockid=22575e2799d1672a38cf48b598b3669d" },
    ],
  },
  {
    name: "React",
    trend: "+38%",
    resources: [
      { title: "React Docs", url: "https://react.dev/learn" },
      { title: "FreeCodeCamp", url: "https://www.freecodecamp.org/news/react-fundamentals-for-beginners/" },
    ],
  },
  {
    name: "Data Engineering",
    trend: "+52%",
    resources: [
      { title: "DataCamp", url: "https://www.datacamp.com/category/data-engineering" },
      { title: "Udacity Nanodegree", url: "https://www.udacity.com/course/data-engineer-nanodegree--nd027" },
    ],
  },
  {
    name: "Cloud Architecture",
    trend: "+41%",
    resources: [
      { title: "AWS Training", url: "https://aws.amazon.com/training/learn-about/architect/" },
      { title: "Azure Fundamentals", url: "https://www.geeksforgeeks.org/cloud-computing/az-900-microsoft-azure-fundamentals/" },
    ],
  },
];

const SkillGrowth = () => {
  return (
    <div className="space-y-6 animate-fade-in">
      <div>
        <h1 className="text-3xl font-bold mb-2 flex items-center gap-2">
          <TrendingUp className="w-8 h-8 text-primary" />
          Skill Growth
        </h1>
        <p className="text-muted-foreground">Trending skills and learning resources for your career growth</p>
      </div>

      <div className="grid md:grid-cols-2 gap-6">
        {trendingSkills.map((skill, index) => (
          <Card
            key={index}
            className="hover:shadow-lg transition-all duration-300 border-2 hover:border-primary group"
          >
            <CardHeader>
              <div className="flex items-center justify-between">
                <CardTitle className="text-xl flex items-center gap-2">
                  <Zap className="w-5 h-5 text-secondary group-hover:text-primary transition-colors" />
                  {skill.name}
                </CardTitle>
                <Badge className="bg-green-100 text-green-700 hover:bg-green-200">
                  {skill.trend}
                </Badge>
              </div>
              <CardDescription>Highly in-demand skill in the market</CardDescription>
            </CardHeader>
            <CardContent className="space-y-3">
              <p className="text-sm font-medium text-muted-foreground">Free Learning Resources:</p>
              <div className="space-y-2">
                {skill.resources.map((resource, idx) => (
                  <Button
                    key={idx}
                    variant="outline"
                    className="w-full justify-between hover:bg-accent"
                    asChild
                  >
                    <a href={resource.url} target="_blank" rel="noopener noreferrer">
                      {resource.title}
                      <ExternalLink className="w-4 h-4" />
                    </a>
                  </Button>
                ))}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default SkillGrowth;
