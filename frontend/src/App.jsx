import React from "react";
import CodeSnippetDisplay from "./components/Snippets";
import Header from "./components/Header";

const App = () => {
  return (
    <div>
      <Header/>
      <CodeSnippetDisplay />
    </div>
  );
};

export default App;
