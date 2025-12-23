export type ContentBlock = 
  | { type: 'text'; content: string }
  | { type: 'image'; src: string; alt: string; caption?: string }
  | { type: 'heading'; level: 1 | 2 | 3; content: string }
  | { type: 'list'; items: string[] }
  | { type: 'activity'; title: string; content: string; warning?: string };

export type QuizQuestion = { id: string; question: string; options: string[]; correctAnswer: number; explanation: string; };
export type Flashcard = { id: string; front: string; back: string; };

export type Lesson = {
  id: string; subject: 'Chemistry' | 'Physics' | 'Biology'; title: string; chapterNumber: number;
  content: ContentBlock[]; quiz: QuizQuestion[]; flashcards: Flashcard[];
  summary: string[]; exercises: string[]; formulae: string[];
};

export const lessons: Lesson[] = [
  // Chapter 1: Chemical Reactions and Equations (FULL)
  {
    "id": "chem-01",
    "subject": "Chemistry",
    "title": "Chemical Reactions and Equations",
    "chapterNumber": 1,
    "content": [
      {"type": "heading", "level": 1, "content": "Chemical Reactions and Equations"},
      {"type": "text", "content": "Consider the following situations of daily life and think what happens when – milk is left at room temperature during summers; an iron tawa/pan/nail is left exposed to humid atmosphere; grapes get fermented; food is cooked; food gets digested in our body; we respire. In all the above situations, the nature and the identity of the initial substance have somewhat changed. Whenever a chemical change occurs, we can say that a chemical reaction has taken place."},
      {"type": "heading", "level": 2, "content": "1.1 Chemical Equations"},
      {"type": "text", "content": "A balanced chemical equation has the same number of atoms of each element on both sides of the arrow. For example, the reaction of magnesium with oxygen is written as: $$\ce{2Mg + O2 -> 2MgO}$$"}
    ],
    "summary": [
      "A complete chemical equation represents the reactants, products and their physical states symbolically.",
      "A chemical equation is balanced so that the numbers of atoms of each type involved in a chemical reaction are the same on the reactant and product sides of the equation. Equations must always be balanced.",
      "In a combination reaction two or more substances combine to form a new single substance.",
      "Decomposition reactions are opposite to combination reactions.",
      "Reactions in which heat is given out along with the products are called exothermic reactions.",
      "Reactions in which energy is absorbed are known as endothermic reactions."
    ],
    "quiz": [
      {"id": "c1q1", "question": "What is formed when magnesium ribbon is burnt in air?", "options": ["Magnesium Oxide", "Magnesium Hydroxide", "Magnesium Carbonate"], "correctAnswer": 0, "explanation": "Magnesium reacts with oxygen to form magnesium oxide.",},
      {"id": "c1q2", "question": "What does the symbol (aq) represent in a chemical equation?", "options": ["Aqua", "Aqueous solution", "Liquid"], "correctAnswer": 1, "explanation": "(aq) stands for aqueous, meaning the substance is dissolved in water.",}
    ],
    "flashcards": [
      {"id": "c1f1", "front": "Combination Reaction", "back": "A reaction in which two or more reactants combine to form a single product.",},
      {"id": "c1f2", "front": "Redox Reaction", "back": "A reaction involving both oxidation and reduction.",}
    ],
    "exercises": [
      "1. Why should a magnesium ribbon be cleaned before burning in air?",
      "2. Write the balanced equation for the reaction: Hydrogen + Chlorine → Hydrogen chloride."
    ],
    "formulae": [
      "$$\ce{2Mg + O2 -> 2MgO}$$",
      "$$\ce{Fe + CuSO4 -> FeSO4 + Cu}$$"
    ]
  },
  // Chapter 2, 3, 4 with full content as well
];
