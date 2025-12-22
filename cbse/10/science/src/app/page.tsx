"use client";

import Link from "next/link";
import { lessons } from "@/data/lessons";
import { useProgress } from "@/context/ProgressContext";
import { CheckCircle, Circle, Book } from "lucide-react";

export default function Dashboard() {
  const { progress } = useProgress();

  // Group lessons by subject
  const subjects = Array.from(new Set(lessons.map(l => l.subject)));

  return (
    <div className="space-y-8">
      <header className="text-center space-y-4">
        <h1 className="text-4xl font-bold text-gray-900">CBSE Class 10 Science</h1>
        <p className="text-xl text-gray-600">Your complete guide to acing the exams</p>
      </header>

      <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
        {subjects.map(subject => (
          <div key={subject} className="bg-white rounded-xl shadow-md overflow-hidden border border-gray-100">
            <div className="bg-primary/10 p-4 border-b border-primary/10">
              <h2 className="text-xl font-semibold text-primary flex items-center gap-2">
                <Book className="w-5 h-5" />
                {subject}
              </h2>
            </div>
            <div className="divide-y divide-gray-100">
              {lessons.filter(l => l.subject === subject).map(lesson => {
                const isCompleted = progress.completedLessons.includes(lesson.id);
                return (
                  <Link 
                    key={lesson.id} 
                    href={`/lesson/${lesson.id}`}
                    className="block p-4 hover:bg-gray-50 transition-colors"
                  >
                    <div className="flex items-start justify-between gap-4">
                      <div>
                        <h3 className="text-base font-medium text-gray-900 mt-1">
                          {lesson.subject} Lesson {lesson.chapterNumber} - {lesson.title}
                        </h3>
                      </div>
                      {isCompleted ? (
                        <CheckCircle className="w-5 h-5 text-green-500 shrink-0" />
                      ) : (
                        <Circle className="w-5 h-5 text-gray-300 shrink-0" />
                      )}
                    </div>
                  </Link>
                );
              })}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
