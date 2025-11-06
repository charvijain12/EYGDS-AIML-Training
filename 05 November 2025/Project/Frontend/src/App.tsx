import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./components/Layout";
import Home from "./pages/Home";
import AddEmployee from "./pages/AddEmployee";
import ExistingEmployees from "./pages/ExistingEmployees";
import ChatAssistant from "./pages/ChatAssistant";
import SkillGrowth from "./pages/SkillGrowth";
import NotFound from "./pages/NotFound";
import Login from "./pages/Login"; // ✅ NEW LOGIN PAGE

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <TooltipProvider>
      <Toaster />
      <Sonner />
      <BrowserRouter>
        <Routes>
          {/* 🧩 LOGIN route without Layout */}
          <Route path="/login" element={<Login />} />

          {/* 🌐 Main app routes inside Layout */}
          <Route
            path="/*"
            element={
              <Layout>
                <Routes>
                  <Route path="/" element={<Home />} />
                  <Route path="/employees" element={<ExistingEmployees />} />
                  <Route path="/add-employee" element={<AddEmployee />} />
                  <Route path="/chat" element={<ChatAssistant />} />
                  <Route path="/skill-growth" element={<SkillGrowth />} />
                  <Route path="*" element={<NotFound />} />
                </Routes>
              </Layout>
            }
          />
        </Routes>
      </BrowserRouter>
    </TooltipProvider>
  </QueryClientProvider>
);

export default App;