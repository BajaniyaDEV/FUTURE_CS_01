import { Card } from "./ui/card";
import { Checkbox } from "./ui/checkbox";
import { Label } from "./ui/label";
import { Clock, Filter } from "lucide-react";

export function FilterSidebar() {
  const timeRanges = [
    { id: "all", name: "All", checked: true },
    { id: "hour", name: "Past Hour", checked: false },
    { id: "day", name: "Past 24 Hours", checked: false },
    { id: "week", name: "Past Week", checked: false },
    { id: "month", name: "Past Month", checked: false },
    { id: "year", name: "Past Year", checked: false },
  ];

  return (
    <div className="w-80 h-full bg-card/20 backdrop-blur-sm border-r border-primary/20 p-4 overflow-y-auto">
      <div className="flex items-center gap-2 mb-6">
        <Filter className="w-5 h-5 text-primary" />
        <h3 className="text-primary">SEARCH FILTERS</h3>
      </div>

      {/* Time Range */}
      <Card className="p-4 mb-4 bg-card/30 backdrop-blur-sm cyber-glow border-primary/20">
        <div className="flex items-center gap-2 mb-3">
          <Clock className="w-4 h-4 text-primary" />
          <Label className="text-primary">Time Range</Label>
        </div>
        <div className="space-y-3">
          {timeRanges.map((range) => (
            <div key={range.id} className="flex items-center space-x-2">
              <Checkbox 
                id={range.id} 
                defaultChecked={range.checked}
                className="border-primary/50 data-[state=checked]:bg-primary data-[state=checked]:border-primary"
              />
              <Label 
                htmlFor={range.id} 
                className="text-sm text-foreground cursor-pointer"
              >
                {range.name}
              </Label>
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
}