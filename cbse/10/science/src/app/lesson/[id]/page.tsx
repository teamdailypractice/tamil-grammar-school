import { lessons } from "@/data/lessons";
import { LessonView } from "@/components/lesson/LessonView";
import { notFound } from "next/navigation";

interface PageProps {
  params: {
    id: string;
  };
}

export function generateStaticParams() {
  return lessons.map((lesson) => ({
    id: lesson.id,
  }));
}

export default function Page({ params }: PageProps) {
  const lesson = lessons.find((l) => l.id === params.id);

  if (!lesson) {
    notFound();
  }

  return <LessonView lesson={lesson} />;
}
