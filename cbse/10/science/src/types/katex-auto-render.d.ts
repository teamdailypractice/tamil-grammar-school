declare module 'katex/dist/contrib/auto-render' {
  import { KaTeXOptions } from 'katex';
  export default function renderMathInElement(element: HTMLElement, options?: KaTeXOptions & { delimiters?: { left: string; right: string; display: boolean }[] }): void;
}
