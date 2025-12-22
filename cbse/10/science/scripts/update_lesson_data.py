import json

def get_content():
    c = []
    c.append({"type": "heading", "level": 1, "content": "Chemical Reactions and Equations"})
    c.append({"type": "text", "content": "Consider the following situations of daily life and think what happens when –\n\n• milk is left at room temperature during summers.\n• an iron tawa/pan/nail is left exposed to humid atmosphere.\n• grapes get fermented.\n• food is cooked.\n• food gets digested in our body.\n• we respire.\n\nIn all the above situations, the nature and the identity of the initial substance have somewhat changed. We have already learnt about physical and chemical changes of matter in our previous classes. Whenever a chemical change occurs, we can say that a chemical reaction has taken place."})
    
    c.append({"type": "heading", "level": 2, "content": "1.1 Chemical Equations"})
    c.append({"type": "activity", "title": "Activity 1.1: Burning of Magnesium Ribbon", "content": "Clean a magnesium ribbon about 3-4 cm long by rubbing it with sandpaper. Hold it with a pair of tongs. Burn it using a spirit lamp or burner and collect the ash so formed in a watch-glass.", "warning": "CAUTION: This Activity needs the teacher’s assistance. It would be better if students wear suitable eyeglasses."})
    c.append({"type": "text", "content": "You must have observed that magnesium ribbon burns with a dazzling white flame and changes into a white powder. This powder is magnesium oxide. It is formed due to the reaction between magnesium and oxygen present in the air."})
    
    c.append({"type": "heading", "level": 3, "content": "Writing a Chemical Equation"})
    c.append({"type": "text", "content": "The simplest way to describe a chemical reaction is in the form of a word-equation. The word-equation for the above reaction would be –\n\nMagnesium + Oxygen → Magnesium oxide\n(Reactants) (Product)\n\nChemical equations can be made more concise and useful if we use chemical formulae instead of words. A chemical equation represents a chemical reaction.\n\n$$\\ce{Mg + O2 -> MgO}$$"})
    
    c.append({"type": "heading", "level": 3, "content": "Balanced Chemical Equations"})
    c.append({"type": "text", "content": "Recall the law of conservation of mass that you studied in Class IX: mass can neither be created nor destroyed in a chemical reaction. That is, the total mass of the elements present in the products of a chemical reaction has to be equal to the total mass of the elements present in the reactants.\n\n$$\\ce{Zn + H2SO4 -> ZnSO4 + H2}$$ "})

    c.append({"type": "heading", "level": 2, "content": "1.2 Types of Chemical Reactions"})
    c.append({"type": "heading", "level": 3, "content": "1.2.1 Combination Reaction"})
    c.append({"type": "activity", "title": "Activity 1.4: Reaction of Calcium Oxide with Water", "content": "Take a small amount of calcium oxide or quick lime in a beaker. Slowly add water to this. Touch the beaker. Do you feel any change in temperature?", "warning": "CAUTION: Handle with care as it's an exothermic reaction."})
    c.append({"type": "text", "content": "Calcium oxide reacts vigorously with water to produce slaked lime (calcium hydroxide) releasing a large amount of heat.\n\n$$\\ce{CaO(s) + H2O(l) -> Ca(OH)2(aq) + Heat}$$ \n\nIn this reaction, calcium oxide and water combine to form a single product, calcium hydroxide. Such a reaction in which a single product is formed from two or more reactants is known as a combination reaction."})
    
    c.append({"type": "heading", "level": 3, "content": "1.2.2 Decomposition Reaction"})
    c.append({"type": "activity", "title": "Activity 1.5: Heating of Ferrous Sulphate", "content": "Take about 2 g ferrous sulphate crystals in a dry boiling tube. Heat the boiling tube over the flame. Observe the colour of the crystals.", "warning": "Observe the colour changes and smell the odour carefully."})
    c.append({"type": "text", "content": "$$\\ce{2FeSO4(s) ->[Heat] Fe2O3(s) + SO2(g) + SO3(g)}$$\\n\nIn this reaction you can observe that a single reactant breaks down to give simpler products. This is a decomposition reaction."})
    
    c.append({"type": "heading", "level": 3, "content": "1.2.3 Displacement Reaction"})
    c.append({"type": "text", "content": "When an element displaces another element from its compound, it is called a displacement reaction.\n\n$$\\ce{Fe(s) + CuSO4(aq) -> FeSO4(aq) + Cu(s)}$$\\n\nIn this reaction, iron has displaced or removed another element, copper, from copper sulphate solution."})

    c.append({"type": "heading", "level": 3, "content": "1.2.4 Double Displacement Reaction"})
    c.append({"type": "text", "content": "Reactions in which there is an exchange of ions between the reactants are called double displacement reactions.\n\n$$\\ce{Na2SO4(aq) + BaCl2(aq) -> BaSO4(s) + 2NaCl(aq)}$$\\n\nA white precipitate of $\\ce{BaSO4}$ is formed by the reaction of $\\ce{SO4^{2-}}$ and $\\ce{Ba^{2+}}$. The other product formed is sodium chloride which remains in the solution."})

    c.append({"type": "heading", "level": 3, "content": "1.2.5 Oxidation and Reduction"})
    c.append({"type": "text", "content": "If a substance gains oxygen during a reaction, it is said to be oxidized. If a substance loses oxygen during a reaction, it is said to be reduced.\n\n$$\\ce{2Cu + O2 ->[Heat] 2CuO}$$ \n\nWhen hydrogen gas is passed over this heated material (\\ce{CuO}), the black coating on the surface turns brown as the reverse reaction takes place and copper is obtained.\n\n$$\\ce{CuO + H2 ->[Heat] Cu + H2O}$$ \n\nIn this reaction, the copper(II) oxide is losing oxygen and is being reduced. The hydrogen is gaining oxygen and is being oxidized. Such reactions are called oxidation-reduction reactions or redox reactions."})

    c.append({"type": "heading", "level": 2, "content": "1.3 Effects of Oxidation Reactions in Everyday Life"})
    c.append({"type": "heading", "level": 3, "content": "Corrosion"})
    c.append({"type": "text", "content": "When a metal is attacked by substances around it such as moisture, acids, etc., it is said to corrode and this process is called corrosion. The black coating on silver and the green coating on copper are other examples of corrosion."})
    c.append({"type": "heading", "level": 3, "content": "Rancidity"})
    c.append({"type": "text", "content": "When fats and oils are oxidized, they become rancid and their smell and taste change. Usually substances which prevent oxidation (antioxidants) are added to foods containing fats and oil."})
    return c

def get_quiz():
    q = []
    q.append({"id": "q1", "question": "Which of the following is a physical change?", "options": ["Formation of curd from milk", "Burning of wood", "Melting of wax", "Rusting of iron"], "correctAnswer": 2, "explanation": "Melting of wax is a physical change because it only changes its state and can be reversed."})
    q.append({"id": "q2", "question": "What is the chemical formula of slaked lime?", "options": ["CaO", "Ca(OH)2", "CaCO3", "CaCl2"], "correctAnswer": 1, "explanation": "Calcium hydroxide $\\ce{Ca(OH)2}$ is known as slaked lime."})
    q.append({"id": "q3", "question": "$$\\ce{Fe2O3 + 2Al -> Al2O3 + 2Fe}$$ is an example of a:", "options": ["Combination reaction", "Double displacement reaction", "Decomposition reaction", "Displacement reaction"], "correctAnswer": 3, "explanation": "Aluminium displaces Iron from its oxide."})
    q.append({"id": "q4", "question": "What happens when dilute hydrochloric acid is added to iron filings?", "options": ["Hydrogen gas and iron chloride are produced", "Chlorine gas and iron hydroxide are produced", "No reaction takes place", "Iron salt and water are produced"], "correctAnswer": 0, "explanation": "$$\\ce{Fe + 2HCl -> FeCl2 + H2}$$ "})
    q.append({"id": "q5", "question": "Which gas is evolved when zinc granules react with dilute sulphuric acid?", "options": ["Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen"], "correctAnswer": 1, "explanation": "$$\\ce{Zn + H2SO4 -> ZnSO4 + H2}$$ "})
    q.append({"id": "q6", "question": "The decomposition of vegetable matter into compost is an example of:", "options": ["Endothermic", "Exothermic", "Displacement", "Redox"], "correctAnswer": 1, "explanation": "It releases energy."})
    q.append({"id": "q7", "question": "A substance 'X' is used for white washing. What is 'X'?", "options": ["Calcium Carbonate", "Calcium Hydroxide", "Calcium Oxide", "Calcium Chloride"], "correctAnswer": 2, "explanation": "Quick lime (CaO) is used."})
    q.append({"id": "q8", "question": "Which is a redox reaction?", "options": ["NaOH + HCl", "BaCl2 + H2SO4", "CuO + H2", "CaCO3 -> CaO"], "correctAnswer": 2, "explanation": "$$\\ce{CuO}$$ is reduced, $\\ce{H2}$ is oxidized."})
    q.append({"id": "q9", "question": "What is the black coating on silver called?", "options": ["Rust", "Corrosion", "Silver sulphide", "Silver oxide"], "correctAnswer": 2, "explanation": "Silver sulphide is formed."})
    q.append({"id": "q10", "question": "Antioxidants prevent:", "options": ["Corrosion", "Rancidity", "Decomposition", "Fermentation"], "correctAnswer": 1, "explanation": "They stop fats from oxidizing."})
    return q

def get_flashcards():
    f = []
    f.append({"id": "f1", "front": "Chemical Reaction", "back": "Transformation of substances into new substances."})
    f.append({"id": "f2", "front": "Balanced Equation", "back": "Equal atoms on both sides."})
    f.append({"id": "f3", "front": "Exothermic Reaction", "back": "Heat is released."})
    f.append({"id": "f4", "front": "Endothermic Reaction", "back": "Energy is absorbed."})
    f.append({"id": "f5", "front": "Combination Reaction", "back": "Two reactants form one product."})
    f.append({"id": "f6", "front": "Decomposition Reaction", "back": "One reactant breaks into multiple products."})
    f.append({"id": "f7", "front": "Displacement Reaction", "back": "More reactive element displaces less reactive one."})
    f.append({"id": "f8", "front": "Double Displacement", "back": "Exchange of ions."})
    f.append({"id": "f9", "front": "Precipitation", "back": "Formation of insoluble solid."})
    f.append({"id": "f10", "front": "Redox Reaction", "back": "Both oxidation and reduction occur."})
    f.append({"id": "f11", "front": "Oxidation", "back": "Gain of oxygen."})
    f.append({"id": "f12", "front": "Reduction", "back": "Loss of oxygen."})
    f.append({"id": "f13", "front": "Corrosion", "back": "Metal destruction by environment."})
    f.append({"id": "f14", "front": "Rancidity", "back": "Oxidation of fats in food."})
    return f

def get_summary():
    return [
        "A complete chemical equation represents the reactants, products and their physical states symbolically.",
        "A chemical equation is balanced so that the numbers of atoms of each type involved in a chemical reaction are the same on the reactant and product sides of the equation. Equations must always be balanced.",
        "In a combination reaction two or more substances combine to form a new single substance.",
        "Decomposition reactions are opposite to combination reactions. In a decomposition reaction, a single substance decomposes to give two or more substances.",
        "Reactions in which heat is given out along with the products are called exothermic reactions.",
        "Reactions in which energy is absorbed are known as endothermic reactions.",
        "When an element displaces another element from its compound, a displacement reaction occurs.",
        "Two different atoms or groups of atoms (ions) are exchanged in double displacement reactions.",
        "Precipitation reactions produce insoluble salts.",
        "Reactions also involve the gain or loss of oxygen or hydrogen by substances. Oxidation is the gain of oxygen or loss of hydrogen. Reduction is the loss of oxygen or gain of hydrogen."
    ]

def get_exercises():
    return [
        "1. Which of the statements about the reaction below are incorrect?\n2PbO(s) + C(s) → 2Pb(s) + CO2(g)\n(a) Lead is getting reduced.\n(b) Carbon dioxide is getting oxidised.\n(c) Carbon is getting oxidised.\n(d) Lead oxide is getting reduced.",
        "2. Fe2O3 + 2Al → Al2O3 + 2Fe\nThe above reaction is an example of a\n(a) combination reaction.\n(b) double displacement reaction.\n(c) decomposition reaction.\n(d) displacement reaction.",
        "3. What happens when dilute hydrochloric acid is added to iron fillings? Tick the correct answer.\n(a) Hydrogen gas and iron chloride are produced.\n(b) Chlorine gas and iron hydroxide are produced.\n(c) No reaction takes place.\n(d) Iron salt and water are produced.",
        "4. What is a balanced chemical equation? Why should chemical equations be balanced?",
        "5. Translate the following statements into chemical equations and then balance them.\n(a) Hydrogen gas combines with nitrogen to form ammonia.\n(b) Hydrogen sulphide gas burns in air to give water and sulpur dioxide.\n(c) Barium chloride reacts with aluminium sulphate to give aluminium chloride and a precipitate of barium sulphate.\n(d) Potassium metal reacts with water to give potassium hydroxide and hydrogen gas."
    ]

def get_formulae():
    return [
        "$$\\ce{Mg + O2 -> MgO}$$ (Burning of Magnesium)",
        "$$\\ce{Zn + H2SO4 -> ZnSO4 + H2}$$ (Zinc and Sulphuric Acid)",
        "$$\\ce{CaO + H2O -> Ca(OH)2 + Heat}$$ (Combination)",
        "$$\\ce{Ca(OH)2 + CO2 -> CaCO3 + H2O}$$ (White washing)",
        "$$\\ce{2FeSO4 ->[Heat] Fe2O3 + SO2 + SO3}$$ (Decomposition)",
        "$$\\ce{CaCO3 ->[Heat] CaO + CO2}$$ (Quick lime)",
        "$$\\ce{Fe + CuSO4 -> FeSO4 + Cu}$$ (Displacement)",
        "$$\\ce{Na2SO4 + BaCl2 -> BaSO4 + 2NaCl}$$ (Precipitation)",
        "$$\\ce{CuO + H2 ->[Heat] Cu + H2O}$$ (Redox)"
    ]

lessson_data = {
    "id": "chem-01",
    "subject": "Chemistry",
    "title": "Chemical Reactions and Equations",
    "chapterNumber": 1,
    "content": get_content(),
    "quiz": get_quiz(),
    "flashcards": get_flashcards(),
    "summary": get_summary(),
    "exercises": get_exercises(),
    "formulae": get_formulae()
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
  summary: string[];
  exercises: string[];
  formulae: string[];
};

"""

with open('src/data/lessons.ts', 'w') as f:
    f.write(ts_header)
    # Using JSON dump and then fixing double escapes if needed, 
    # but the primary issue was 'r' strings + f-strings in python.
    f.write(f"export const lessons: Lesson[] = {json.dumps([lesson_data], indent=2)};\n")
