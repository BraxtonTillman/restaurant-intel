"use client";

import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState(null);

  function handleDrop(e) {
    e.preventDefault();
    const droppedFile = e.dataTransfer.files[0];
    if (droppedFile.type === "text/csv") {
      setFile(droppedFile);
    } else {
      alert("Please drop a CSV file");
    }
  }

  return (
    <div className="flex items-center justify-center h-screen">
      <div
        className="border-2 border-dashed border-blue-400 w-96 h-48 hover:bg-blue-50"
        onDragOver={(e) => e.preventDefault()}
        onDrop={handleDrop}
      >
        <p className="flex items-center justify-center">Drop a CSV here</p>
        {file && (
          <p className="flex items-center justify-center text-green-600">
            File ready: {file.name}
          </p>
        )}
      </div>
    </div>
  );
}
