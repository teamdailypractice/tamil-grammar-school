"use client";

import { useState } from "react";
import { Flashcard } from "@/data/lessons";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { cn } from "@/lib/utils";
import { SmartText } from "@/components/ui/LatexRenderer";

interface FlashcardDeckProps {
  cards: Flashcard[];
}

export function FlashcardDeck({ cards }: FlashcardDeckProps) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);

  const handleNext = () => {
    setIsFlipped(false);
    setTimeout(() => {
      setCurrentIndex((prev) => (prev + 1) % cards.length);
    }, 150);
  };

  const handlePrev = () => {
    setIsFlipped(false);
    setTimeout(() => {
      setCurrentIndex((prev) => (prev - 1 + cards.length) % cards.length);
    }, 150);
  };

  const currentCard = cards[currentIndex];

  return (
    <div className="max-w-xl mx-auto space-y-8 py-8">
      <div 
        className="relative h-64 w-full perspective-1000 cursor-pointer group"
        onClick={() => setIsFlipped(!isFlipped)}
      >
        <div className={cn(
          "w-full h-full duration-500 preserve-3d transition-transform relative",
          isFlipped ? "rotate-y-180" : ""
        )}>
          {/* Front */}
          <div className="absolute inset-0 backface-hidden bg-white rounded-2xl shadow-lg border border-gray-100 flex flex-col items-center justify-center p-8 text-center">
            <span className="text-sm font-medium text-primary uppercase tracking-wider mb-4">Question</span>
            <h3 className="text-2xl font-bold text-gray-900">
              <SmartText text={currentCard.front} />
            </h3>
            <p className="text-xs text-gray-400 absolute bottom-4">Click to flip</p>
          </div>

          {/* Back */}
          <div className="absolute inset-0 backface-hidden rotate-y-180 bg-primary rounded-2xl shadow-lg flex flex-col items-center justify-center p-8 text-center text-white">
            <span className="text-sm font-medium text-white/80 uppercase tracking-wider mb-4">Answer</span>
            <p className="text-xl font-medium">
              <SmartText text={currentCard.back} />
            </p>
          </div>
        </div>
      </div>

      <div className="flex items-center justify-between px-4">
        <button
          onClick={(e) => { e.stopPropagation(); handlePrev(); }}
          className="p-2 rounded-full hover:bg-gray-100 text-gray-600 transition-colors"
        >
          <ChevronLeft className="w-6 h-6" />
        </button>
        <span className="text-sm font-medium text-gray-500">
          {currentIndex + 1} / {cards.length}
        </span>
        <button
          onClick={(e) => { e.stopPropagation(); handleNext(); }}
          className="p-2 rounded-full hover:bg-gray-100 text-gray-600 transition-colors"
        >
          <ChevronRight className="w-6 h-6" />
        </button>
      </div>

      <style jsx global>{`
        .perspective-1000 { perspective: 1000px; }
        .preserve-3d { transform-style: preserve-3d; }
        .rotate-y-180 { transform: rotateY(180deg); }
        .backface-hidden { backface-visibility: hidden; }
      `}</style>
    </div>
  );
}