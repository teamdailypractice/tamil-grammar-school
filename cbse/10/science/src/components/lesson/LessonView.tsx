"use client";

import { useState, useEffect } from "react";
import { Lesson } from "@/data/lessons";
import { LessonContent } from "./LessonContent";
import { QuizComponent } from "../quiz/QuizComponent";
import { FlashcardDeck } from "../flashcards/FlashcardDeck";
import { PDFDownload } from "./PDFDownload";
import { useProgress } from "@/context/ProgressContext";
import { BookOpen, BrainCircuit, PenTool, CheckCircle, Download } from "lucide-react";
import { cn } from "@/lib/utils";
import { SmartText } from "@/components/ui/LatexRenderer";

export function LessonView({ lesson }: { lesson: Lesson }) {
  const [activeTab, setActiveTab] = useState<'content' | 'quiz' | 'flashcards' | 'summary' | 'formulae' | 'exercises'>('content');
  const { markLessonComplete, progress } = useProgress();

  useEffect(() => {
    markLessonComplete(lesson.id);
  }, [lesson.id, markLessonComplete]);

  const tabs = [
    { id: 'content', label: 'Lesson', icon: BookOpen },
    { id: 'summary', label: 'Summary', icon: CheckCircle },
    { id: 'formulae', label: 'Revision', icon: PenTool },
    { id: 'flashcards', label: 'Flashcards', icon: BrainCircuit },
    { id: 'quiz', label: 'Quiz', icon: PenTool },
    { id: 'exercises', label: 'Exercises', icon: BookOpen },
  ] as const;

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-white p-6 rounded-xl shadow-sm border">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">{lesson.title}</h1>
          <p className="text-gray-500">Chapter {lesson.chapterNumber} • {lesson.subject}</p>
        </div>
        <div className="flex items-center gap-4">
          {progress.completedLessons.includes(lesson.id) && (
            <div className="flex items-center text-green-600 bg-green-50 px-3 py-1 rounded-full text-sm font-medium">
              <CheckCircle className="w-4 h-4 mr-1.5" />
              Completed
            </div>
          )}
          {activeTab === 'content' && (
            <div className="flex gap-2">
              <a 
                href={`/downloads/${lesson.id}.pdf`} 
                download
                className="inline-flex items-center px-4 py-2 bg-white border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors"
              >
                <Download className="w-4 h-4 mr-2" />
                PDF
              </a>
              <a 
                href={`/downloads/${lesson.id}.epub`} 
                download
                className="inline-flex items-center px-4 py-2 bg-white border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors"
              >
                <Download className="w-4 h-4 mr-2" />
                EPUB
              </a>
            </div>
          )}
        </div>
      </div>

      <div className="bg-white rounded-xl shadow-sm border overflow-hidden min-h-[600px]">
        <div className="border-b">
          <nav className="flex" aria-label="Tabs">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={cn(
                    "flex-1 py-4 px-1 text-center border-b-2 font-medium text-sm flex items-center justify-center gap-2 transition-colors",
                    activeTab === tab.id
                      ? "border-primary text-primary bg-primary/5"
                      : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
                  )}
                >
                  <Icon className="w-4 h-4" />
                  {tab.label}
                </button>
              );
            })}
          </nav>
        </div>

        <div className="p-6">
          {activeTab === 'content' && <LessonContent content={lesson.content} />}
          {activeTab === 'summary' && (
            <div className="space-y-6">
              <h2 className="text-2xl font-bold">What you have learnt</h2>
              <ul className="list-disc pl-6 space-y-4">
                {lesson.summary.map((item, i) => (
                  <li key={i} className="text-gray-700 leading-relaxed"><SmartText text={item} /></li>
                ))}
              </ul>
            </div>
          )}
          {activeTab === 'formulae' && (
            <div className="space-y-6">
              <h2 className="text-2xl font-bold">Equations & Formulae</h2>
              <div className="grid gap-4">
                {lesson.formulae.map((item, i) => (
                  <div key={i} className="p-4 bg-gray-50 rounded-lg border border-gray-100">
                    <SmartText text={item} />
                  </div>
                ))}
              </div>
            </div>
          )}
          {activeTab === 'exercises' && (
            <div className="space-y-6">
              <h2 className="text-2xl font-bold">Exercises</h2>
              <div className="space-y-8">
                {lesson.exercises.map((item, i) => (
                  <div key={i} className="text-gray-700 leading-relaxed whitespace-pre-wrap">
                    <SmartText text={item} />
                  </div>
                ))}
              </div>
            </div>
          )}
          {activeTab === 'quiz' && <QuizComponent lessonId={lesson.id} questions={lesson.quiz} />}
          {activeTab === 'flashcards' && <FlashcardDeck cards={lesson.flashcards} />}
        </div>
      </div>
    </div>
  );
}
