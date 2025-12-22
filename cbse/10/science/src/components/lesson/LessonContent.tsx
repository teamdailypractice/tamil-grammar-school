"use client";

import { ContentBlock } from "@/data/lessons";
import { AlertTriangle } from "lucide-react";
import { SmartText } from "@/components/ui/LatexRenderer";

export function LessonContent({ content }: { content: ContentBlock[] }) {
  return (
    <div className="prose prose-blue max-w-none space-y-8" id="lesson-content">
      {content.map((block, index) => {
        switch (block.type) {
          case 'heading':
            const H = `h${block.level}` as keyof JSX.IntrinsicElements;
            return (
              <H key={index} className="font-bold text-gray-900 mt-8 mb-4">
                <SmartText text={block.content} />
              </H>
            );
          
          case 'text':
            return (
              <p key={index} className="text-gray-700 leading-relaxed whitespace-pre-wrap">
                <SmartText text={block.content} />
              </p>
            );
          
          case 'image':
            return null; // Images ignored as requested

          case 'list':
            return (
              <ul key={index} className="list-disc pl-6 space-y-2 text-gray-700">
                {block.items.map((item, i) => (
                  <li key={i}><SmartText text={item} /></li>
                ))}
              </ul>
            );

          case 'activity':
            return (
              <div key={index} className="bg-yellow-50 border-l-4 border-yellow-400 p-6 rounded-r-lg my-8">
                <h3 className="text-lg font-bold text-yellow-800 mb-2">
                  <SmartText text={block.title} />
                </h3>
                <p className="text-yellow-800 mb-4">
                  <SmartText text={block.content} />
                </p>
                {block.warning && (
                  <div className="flex items-start gap-2 text-sm text-yellow-700 bg-yellow-100 p-3 rounded">
                    <AlertTriangle className="w-5 h-5 shrink-0" />
                    <span><SmartText text={block.warning} /></span>
                  </div>
                )}
              </div>
            );
            
          default:
            return null;
        }
      })}
    </div>
  );
}
