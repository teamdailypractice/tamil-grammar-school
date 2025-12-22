"use client";

import { useState } from "react";
import { QuizQuestion } from "@/data/lessons";
import { Check, X, RefreshCw } from "lucide-react";
import { useProgress } from "@/context/ProgressContext";
import { cn } from "@/lib/utils";
import { SmartText } from "@/components/ui/LatexRenderer";

interface QuizProps {
  lessonId: string;
  questions: QuizQuestion[];
}

export function QuizComponent({ lessonId, questions }: QuizProps) {
  const { saveQuizScore } = useProgress();
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedOption, setSelectedOption] = useState<number | null>(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [score, setScore] = useState(0);
  const [showResults, setShowResults] = useState(false);

  const handleOptionSelect = (index: number) => {
    if (isAnswered) return;
    setSelectedOption(index);
    setIsAnswered(true);

    if (index === questions[currentQuestion].correctAnswer) {
      setScore(s => s + 1);
    }
  };

  const nextQuestion = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(c => c + 1);
      setSelectedOption(null);
      setIsAnswered(false);
    } else {
      finishQuiz();
    }
  };

  const finishQuiz = () => {
    setShowResults(true);
    const percentage = Math.round((score / questions.length) * 100);
    saveQuizScore(lessonId, percentage);
  };

  const restartQuiz = () => {
    setCurrentQuestion(0);
    setSelectedOption(null);
    setIsAnswered(false);
    setScore(0);
    setShowResults(false);
  };

  if (showResults) {
    return (
      <div className="text-center p-8 bg-white rounded-xl shadow-sm border space-y-6">
        <h3 className="text-2xl font-bold">Quiz Completed!</h3>
        <div className="text-4xl font-black text-primary">
          {Math.round((score / questions.length) * 100)}%
        </div>
        <p className="text-gray-600">You scored {score} out of {questions.length}</p>
        <button
          onClick={restartQuiz}
          className="inline-flex items-center px-4 py-2 bg-primary text-white rounded-lg hover:bg-primary/90"
        >
          <RefreshCw className="w-4 h-4 mr-2" />
          Try Again
        </button>
      </div>
    );
  }

  const question = questions[currentQuestion];

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div className="flex justify-between items-center text-sm text-gray-500">
        <span>Question {currentQuestion + 1} of {questions.length}</span>
        <span>Score: {score}</span>
      </div>

      <div className="bg-white p-6 rounded-xl shadow-sm border space-y-4">
        <h3 className="text-lg font-medium">
          <SmartText text={question.question} />
        </h3>

        <div className="space-y-3">
          {question.options.map((option, index) => {
            let stateStyle = "border-gray-200 hover:border-primary hover:bg-primary/5";
            if (isAnswered) {
              if (index === question.correctAnswer) {
                stateStyle = "border-green-500 bg-green-50 text-green-700";
              } else if (index === selectedOption) {
                stateStyle = "border-red-500 bg-red-50 text-red-700";
              } else {
                stateStyle = "border-gray-100 text-gray-400";
              }
            }

            return (
              <button
                key={index}
                onClick={() => handleOptionSelect(index)}
                disabled={isAnswered}
                className={cn(
                  "w-full text-left p-4 rounded-lg border-2 transition-all flex justify-between items-center",
                  stateStyle
                )}
              >
                <span><SmartText text={option} /></span>
                {isAnswered && index === question.correctAnswer && (
                  <Check className="w-5 h-5 text-green-600" />
                )}
                {isAnswered && index === selectedOption && index !== question.correctAnswer && (
                  <X className="w-5 h-5 text-red-600" />
                )}
              </button>
            );
          })}
        </div>

        {isAnswered && (
          <div className="pt-4 border-t mt-4">
            <p className="text-sm text-gray-600 mb-4">
              <span className="font-bold">Explanation:</span> <SmartText text={question.explanation} />
            </p>
            <button
              onClick={nextQuestion}
              className="w-full py-3 bg-primary text-white rounded-lg font-medium hover:bg-primary/90"
            >
              {currentQuestion < questions.length - 1 ? "Next Question" : "See Results"}
            </button>
          </div>
        )}
      </div>
    </div>
  );
}