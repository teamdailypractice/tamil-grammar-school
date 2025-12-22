"use client";

import React, { createContext, useContext, useEffect, useState } from "react";

type Progress = {
  completedLessons: string[];
  quizScores: Record<string, number>;
};

type ProgressContextType = {
  progress: Progress;
  markLessonComplete: (lessonId: string) => void;
  saveQuizScore: (lessonId: string, score: number) => void;
};

const ProgressContext = createContext<ProgressContextType | undefined>(undefined);

export function ProgressProvider({ children }: { children: React.ReactNode }) {
  const [progress, setProgress] = useState<Progress>({
    completedLessons: [],
    quizScores: {},
  });

  useEffect(() => {
    const saved = localStorage.getItem("cbse-science-progress");
    if (saved) {
      setProgress(JSON.parse(saved));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem("cbse-science-progress", JSON.stringify(progress));
  }, [progress]);

  const markLessonComplete = (lessonId: string) => {
    if (!progress.completedLessons.includes(lessonId)) {
      setProgress((prev) => ({
        ...prev,
        completedLessons: [...prev.completedLessons, lessonId],
      }));
    }
  };

  const saveQuizScore = (lessonId: string, score: number) => {
    setProgress((prev) => ({
      ...prev,
      quizScores: {
        ...prev.quizScores,
        [lessonId]: Math.max(prev.quizScores[lessonId] || 0, score),
      },
    }));
  };

  return (
    <ProgressContext.Provider value={{ progress, markLessonComplete, saveQuizScore }}>
      {children}
    </ProgressContext.Provider>
  );
}

export function useProgress() {
  const context = useContext(ProgressContext);
  if (context === undefined) {
    throw new Error("useProgress must be used within a ProgressProvider");
  }
  return context;
}
