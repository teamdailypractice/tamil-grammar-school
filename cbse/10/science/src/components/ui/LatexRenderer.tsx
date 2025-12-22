"use client";

import React, { useEffect, useRef } from 'react';
import renderMathInElement from 'katex/dist/contrib/auto-render';
import 'katex/dist/contrib/mhchem.js';

export function SmartText({ text }: { text: string }) {
  const containerRef = useRef<HTMLSpanElement>(null);

  useEffect(() => {
    if (containerRef.current) {
      renderMathInElement(containerRef.current, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
        ],
        throwOnError: false,
        trust: true,
      });
    }
  }, [text]);

  if (!text) return null;

  // We use <span> to avoid "div in p" hydration errors
  // We use suppressHydrationWarning because KaTeX will modify the DOM immediately after hydration
  return (
    <span ref={containerRef} className="inline-block w-full" suppressHydrationWarning>
      {text.split('\n').map((line, i) => (
        <React.Fragment key={i}>
          {line}
          {i < text.split('\n').length - 1 && <br />}
        </React.Fragment>
      ))}
    </span>
  );
}
