import { lessons } from "../src/data/lessons";
import * as fs from "fs";
import * as path from "path";

const outputPath = path.join(__dirname, "lessons.json");
fs.writeFileSync(outputPath, JSON.stringify(lessons, null, 2));
console.log(`Exported ${lessons.length} lessons to ${outputPath}`);
