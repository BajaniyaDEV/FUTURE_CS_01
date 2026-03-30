import { Button } from "./components/ui/button";
import { Input } from "./components/ui/input";
import { ImageWithFallback } from "./components/figma/ImageWithFallback";
import { Card } from "./components/ui/card";
import { Badge } from "./components/ui/badge";
import { CyberBackground } from "./components/CyberBackground";
import { FilterSidebar } from "./components/FilterSidebar";
import {
  Play,
  Square,
  RotateCcw,
  Search,
  Camera,
} from "lucide-react";
import { useState } from "react";

export default function App() {
  const [searchQuery, setSearchQuery] = useState("");

  const handleStart = () => {
    console.log("Start clicked with query:", searchQuery);
  };

  const handleStop = () => {
    console.log("Stop clicked");
  };

  const handleRefresh = () => {
    console.log("Refresh clicked");
  };

  const handleScreenshot = () => {
    console.log("Screenshot clicked");
  };

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Search:", searchQuery);
  };

  return (
    <div className="min-h-screen bg-background relative overflow-hidden">
      <CyberBackground />

      {/* Main content */}
      <div className="relative z-10 flex flex-col h-screen">
        {/* Header with enhanced styling */}
        <header className="border-b border-primary/20 bg-card/10 backdrop-blur-sm flex-shrink-0">
          <div className="flex items-center justify-between max-w-full mx-auto p-6">
            <div className="flex items-center gap-6">
              <div className="relative">
                <ImageWithFallback
                  src="https://pbs.twimg.com/profile_images/1579353190239125505/eJQ6CjIk_400x400.jpg"
                  alt="CID Cyber Crime Logo"
                  className="w-20 h-20 rounded-lg object-cover cyber-glow pulse-glow"
                />
                <div className="absolute -inset-1 rounded-lg border border-primary/30 animate-pulse"></div>
              </div>
              <div>
                <h1 className="text-primary cyber-glow-text mb-1">
                  CID CYBER CRIME
                </h1>
                <Badge
                  variant="outline"
                  className="border-green-500/50 text-green-400 bg-green-500/10"
                >
                  DIVISION
                </Badge>
              </div>
            </div>

            <div className="flex items-center gap-4">
              {/* Search Box */}
              <form
                onSubmit={handleSearch}
                className="relative"
              >
                <div className="relative">
                  <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-muted-foreground" />
                  <Input
                    type="text"
                    placeholder="Enter search query..."
                    value={searchQuery}
                    onChange={(e) =>
                      setSearchQuery(e.target.value)
                    }
                    className="pl-10 w-80 bg-input-background border-primary/30 focus:border-primary cyber-glow"
                  />
                </div>
              </form>

              <div className="flex items-center gap-3">
                <Button
                  onClick={handleStart}
                  className="cyber-button bg-primary hover:bg-primary/80 text-primary-foreground border border-primary/50"
                  variant="default"
                >
                  <Play className="w-4 h-4 mr-2" />
                  START
                </Button>

                <Button
                  onClick={handleStop}
                  className="cyber-button bg-destructive/80 hover:bg-destructive text-white border border-destructive/50"
                  variant="destructive"
                >
                  <Square className="w-4 h-4 mr-2" />
                  STOP
                </Button>

                <Button
                  onClick={handleRefresh}
                  className="cyber-button bg-secondary hover:bg-secondary/80 border border-primary/30"
                  variant="outline"
                >
                  <RotateCcw className="w-4 h-4 mr-2" />
                  REFRESH
                </Button>

                <Button
                  onClick={handleScreenshot}
                  className="cyber-button bg-green-600/80 hover:bg-green-600 text-white border border-green-500/50"
                  variant="secondary"
                >
                  <Camera className="w-4 h-4 mr-2" />
                  SCREENSHOT
                </Button>
              </div>
            </div>
          </div>
        </header>

        {/* Main layout with sidebar and content */}
        <div className="flex flex-1 overflow-hidden">
          {/* Left Sidebar */}
          <FilterSidebar />

          {/* Main Content Area */}
          <main className="flex-1 p-6 overflow-y-auto">
            <Card className="h-full bg-card/20 backdrop-blur-sm cyber-glow border-primary/20 p-6">
              <div className="flex items-center justify-center h-full">
                <div className="text-center">
                  <div className="w-20 h-20 rounded-full bg-primary/20 border-2 border-primary flex items-center justify-center mb-4 mx-auto pulse-glow">
                    <Search className="w-10 h-10 text-primary" />
                  </div>
                  <h2 className="text-xl text-primary mb-2">
                    SEARCH RESULTS
                  </h2>
                  <p className="text-muted-foreground mb-4">
                    Enter a search query and click START to
                    begin monitoring
                  </p>
                  <Badge
                    variant="outline"
                    className="border-primary/50 text-primary/80"
                  >
                    READY FOR INPUT
                  </Badge>
                </div>
              </div>
            </Card>
          </main>
        </div>
      </div>
    </div>
  );
}