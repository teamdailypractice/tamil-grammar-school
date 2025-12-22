import json

def get_content():
    return [
        {"type": "heading", "level": 1, "content": "Chemical Reactions and Equations"},
        {"type": "text", "content": "Consider the following situations of daily life and think what happens when –\n\n• milk is left at room temperature during summers.\n• an iron tawa/pan/nail is left exposed to humid atmosphere.\n• grapes get fermented.\n• food is cooked.\n• food gets digested in our body.\n• we respire.\n\nIn all the above situations, the nature and the identity of the initial substance have somewhat changed. We have already learnt about physical and chemical changes of matter in our previous classes. Whenever a chemical change occurs, we can say that a chemical reaction has taken place."},
        
        {"type": "heading", "level": 2, "content": "1.1 Chemical Equations"},
        {"type": "activity", "title": "Activity 1.1: Burning of Magnesium Ribbon", "content": "Clean a magnesium ribbon about 3-4 cm long by rubbing it with sandpaper. Hold it with a pair of tongs. Burn it using a spirit lamp or burner and collect the ash so formed in a watch-glass.", "warning": "CAUTION: This Activity needs the teacher’s assistance. It would be better if students wear suitable eyeglasses."},        {"type": "text", "content": "You must have observed that magnesium ribbon burns with a dazzling white flame and changes into a white powder. This powder is magnesium oxide. It is formed due to the reaction between magnesium and oxygen present in the air."},
        
        {"type": "heading", "level": 3, "content": "Writing a Chemical Equation"},
        {"type": "text", "content": "The simplest way to describe a chemical reaction is in the form of a word-equation. The word-equation for the above reaction would be –\n\nMagnesium + Oxygen → Magnesium oxide\n(Reactants) (Product)\n\nChemical equations can be made more concise and useful if we use chemical formulae instead of words. A chemical equation represents a chemical reaction.\n\n$$\\ce{Mg + O2 -> MgO}$$"},
        
        {"type": "heading", "level": 3, "content": "Balanced Chemical Equations"},
        {"type": "text", "content": "Recall the law of conservation of mass that you studied in Class IX: mass can neither be created nor destroyed in a chemical reaction. That is, the total mass of the elements present in the products of a chemical reaction has to be equal to the total mass of the elements present in the reactants.\n\n$$\\ce{Zn + H2SO4 -> ZnSO4 + H2}$$"},

        {"type": "heading", "level": 2, "content": "1.2 Types of Chemical Reactions"},
        
        {"type": "heading", "level": 3, "content": "1.2.1 Combination Reaction"},
        {"type": "activity", "title": "Activity 1.4: Reaction of Calcium Oxide with Water", "content": "Take a small amount of calcium oxide or quick lime in a beaker. Slowly add water to this. Touch the beaker. Do you feel any change in temperature?", "warning": "CAUTION: Handle with care as it's an exothermic reaction."},
        {"type": "text", "content": "Calcium oxide reacts vigorously with water to produce slaked lime (calcium hydroxide) releasing a large amount of heat.\n\n$$\\ce{CaO(s) + H2O(l) -> Ca(OH)2(aq) + Heat}$$\\nIn this reaction, calcium oxide and water combine to form a single product, calcium hydroxide. Such a reaction in which a single product is formed from two or more reactants is known as a combination reaction."},
        
        {"type": "heading", "level": 3, "content": "1.2.2 Decomposition Reaction"},
        {"type": "activity", "title": "Activity 1.5: Heating of Ferrous Sulphate", "content": "Take about 2 g ferrous sulphate crystals in a dry boiling tube. Heat the boiling tube over the flame. Observe the colour of the crystals.", "warning": "Observe the colour changes and smell the odour carefully."},
        {"type": "text", "content": "$$\\ce{2FeSO4(s) ->[Heat] Fe2O3(s) + SO2(g) + SO3(g)}$$\\nIn this reaction you can observe that a single reactant breaks down to give simpler products. This is a decomposition reaction."},
        
        {"type": "heading", "level": 3, "content": "1.2.3 Displacement Reaction"},
        {"type": "text", "content": "When an element displaces another element from its compound, it is called a displacement reaction.\n\n$$\\ce{Fe(s) + CuSO4(aq) -> FeSO4(aq) + Cu(s)}$$\\nIn this reaction, iron has displaced or removed another element, copper, from copper sulphate solution."},

        {"type": "heading", "level": 3, "content": "1.2.4 Double Displacement Reaction"},
        {"type": "text", "content": "Reactions in which there is an exchange of ions between the reactants are called double displacement reactions.\n\n$$\\ce{Na2SO4(aq) + BaCl2(aq) -> BaSO4(s) + 2NaCl(aq)}$$\\nA white precipitate of $\\ce{BaSO4}$ is formed by the reaction of $\\ce{SO4^{2-}}$ and $\\ce{Ba^{2+}}$. The other product formed is sodium chloride which remains in the solution."},

        {"type": "heading", "level": 3, "content": "1.2.5 Oxidation and Reduction"},
        {"type": "text", "content": "If a substance gains oxygen during a reaction, it is said to be oxidized. If a substance loses oxygen during a reaction, it is said to be reduced.\n\n$$\\ce{2Cu + O2 ->[Heat] 2CuO}$$\\nWhen hydrogen gas is passed over this heated material ($\\ce{CuO}$), the black coating on the surface turns brown as the reverse reaction takes place and copper is obtained.\n\n$$\\ce{CuO + H2 ->[Heat] Cu + H2O}$$\\nIn this reaction, the copper(II) oxide is losing oxygen and is being reduced. The hydrogen is gaining oxygen and is being oxidized. Such reactions are called oxidation-reduction reactions or redox reactions."},

        {"type": "heading", "level": 2, "content": "1.3 Effects of Oxidation Reactions in Everyday Life"},        {"type": "heading", "level": 3, "content": "Corrosion"},        {"type": "text", "content": "When a metal is attacked by substances around it such as moisture, acids, etc., it is said to corrode and this process is called corrosion. The black coating on silver and the green coating on copper are other examples of corrosion."},        {"type": "heading", "level": 3, "content": "Rancidity"},        {"type": "text", "content": "When fats and oils are oxidized, they become rancid and their smell and taste change. Usually substances which prevent oxidation (antioxidants) are added to foods containing fats and oil."}    ]

def get_quiz():
    return [
        {"id": "q1", "question": "Which of the following is a physical change?", "options": ["Formation of curd from milk", "Burning of wood", "Melting of wax", "Rusting of iron"], "correctAnswer": 2, "explanation": "Melting of wax is a physical change because it only changes its state and can be reversed. Others are chemical changes."},        {"id": "q2", "question": "What is the chemical formula of slaked lime?", "options": ["CaO", "Ca(OH)2", "CaCO3", "CaCl2"], "correctAnswer": 1, "explanation": "Calcium hydroxide Ca(OH)2 is known as slaked lime."},        {"id": "q3", "question": "The reaction $\\ce{Fe2O3 + 2Al -> Al2O3 + 2Fe}$ is an example of a:", "options": ["Combination reaction", "Double displacement reaction", "Decomposition reaction", "Displacement reaction"], "correctAnswer": 3, "explanation": "Aluminium displaces Iron from its oxide, so it is a displacement reaction."},        {"id": "q4", "question": "What happens when dilute hydrochloric acid is added to iron filings?", "options": ["Hydrogen gas and iron chloride are produced", "Chlorine gas and iron hydroxide are produced", "No reaction takes place", "Iron salt and water are produced"], "correctAnswer": 0, "explanation": "$\\ce{Fe + 2HCl -> FeCl2 + H2}$. Hydrogen gas and iron(II) chloride are formed."},        {"id": "q5", "question": "Which gas is evolved when zinc granules react with dilute sulphuric acid?", "options": ["Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen"], "correctAnswer": 1, "explanation": "$\\ce{Zn + H2SO4 -> ZnSO4 + H2}$. Hydrogen gas is evolved."},        {"id": "q6", "question": "The decomposition of vegetable matter into compost is an example of:", "options": ["Endothermic reaction", "Exothermic reaction", "Displacement reaction", "Redox reaction"], "correctAnswer": 1, "explanation": "Decomposition of vegetable matter releases energy, so it is exothermic."},        {"id": "q7", "question": "A substance 'X' is used for white washing. What is 'X'?", "options": ["Calcium Carbonate", "Calcium Hydroxide", "Calcium Oxide", "Calcium Chloride"], "correctAnswer": 2, "explanation": "Quick lime (CaO) is used to prepare slaked lime for white washing."},        {"id": "q8", "question": "Which of the following is an example of a redox reaction?", "options": ["NaOH + HCl -> NaCl + H2O", "BaCl2 + H2SO4 -> BaSO4 + 2HCl", "CuO + H2 -> Cu + H2O", "CaCO3 -> CaO + CO2"], "correctAnswer": 2, "explanation": "In $\\ce{CuO + H2 -> Cu + H2O}$, Copper is reduced and Hydrogen is oxidized."},        {"id": "q9", "question": "What is the black coating on silver called?", "options": ["Rust", "Corrosion", "Silver sulphide", "Silver oxide"], "correctAnswer": 2, "explanation": "Silver reacts with sulphur in the air to form a black coating of silver sulphide."},        {"id": "q10", "question": "Antioxidants are added to food to prevent:", "options": ["Corrosion", "Rancidity", "Decomposition", "Fermentation"], "correctAnswer": 1, "explanation": "Antioxidants prevent oxidation of fats and oils, thus preventing rancidity."}    ]

def get_flashcards():
    return [
        {"id": "f1", "front": "Chemical Reaction", "back": "A process where one or more substances are transformed into new substances."},
        {"id": "f2", "front": "Balanced Equation", "back": "An equation where the number of atoms of each element is equal on both sides."},
        {"id": "f3", "front": "Exothermic Reaction", "back": "A reaction in which heat is released along with products."},
        {"id": "f4", "front": "Endothermic Reaction", "back": "A reaction in which energy is absorbed."},
        {"id": "f5", "front": "Combination Reaction", "back": "A reaction where two or more reactants combine to form a single product."},
        {"id": "f6", "front": "Decomposition Reaction", "back": "A reaction where a single reactant breaks down into two or more products."},
        {"id": "f7", "front": "Displacement Reaction", "back": "A reaction where a more reactive element displaces a less reactive element from its compound."},
        {"id": "f8", "front": "Double Displacement", "back": "A reaction where there is an exchange of ions between reactants."},
        {"id": "f9", "front": "Precipitation Reaction", "back": "A reaction that produces an insoluble solid (precipitate)."},
        {"id": "f10", "front": "Redox Reaction", "back": "A reaction involving both oxidation and reduction."},
        {"id": "f11", "front": "Oxidation", "back": "The gain of oxygen or loss of hydrogen/electrons."},
        {"id": "f12", "front": "Reduction", "back": "The loss of oxygen or gain of hydrogen/electrons."},
        {"id": "f13", "front": "Corrosion", "back": "The gradual destruction of metals by chemical reaction with the environment."},
        {"id": "f14", "front": "Rancidity", "back": "The oxidation of fats and oils in food resulting in bad smell and taste."}    ]

lesson_data = {
    "id": "chem-01",
    "subject": "Chemistry",
    "title": "Chemical Reactions and Equations",
    "chapterNumber": 1,
    "content": get_content(),
    "quiz": get_quiz(),
    "flashcards": get_flashcards()
}

ts_header = """
export type ContentBlock = 
  | { type: 'text'; content: string }
  | { type: 'image'; src: string; alt: string; caption?: string }
  | { type: 'heading'; level: 1 | 2 | 3; content: string }
  | { type: 'list'; items: string[] }
  | { type: 'activity'; title: string; content: string; warning?: string };

export type QuizQuestion = {
  id: string;
  question: string;
  options: string[];
  correctAnswer: number;
  explanation: string;
};

export type Flashcard = {
  id: string;
  front: string;
  back: string;
};

export type Lesson = {
  id: string;
  subject: 'Chemistry' | 'Physics' | 'Biology';
  title: string;
  chapterNumber: number;
  content: ContentBlock[];
  quiz: QuizQuestion[];
  flashcards: Flashcard[];
};

"""

with open('src/data/lessons.ts', 'w') as f:
    f.write(ts_header)
    f.write(f"export const lessons: Lesson[] = {json.dumps([lesson_data], indent=2)};\n")
