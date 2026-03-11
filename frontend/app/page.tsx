"use client";

import { uploadCSV } from "@/lib/api";
import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState<"idle" | "success" | "error">("idle");

  function handleDrop(e) {
    e.preventDefault();
    const droppedFile = e.dataTransfer.files[0];
    if (droppedFile.type === "text/csv") {
      setFile(droppedFile);
    } else {
      alert("Please drop a CSV file");
    }
  }

  async function handleUpload() {
    try {
      await uploadCSV(file);
      setStatus("success");
    } catch (err) {
      console.error(err);
      setStatus("error");
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
        {status === "success" && <p>Uploaded successfully!</p>}
        {status === "error" && <p>Upload failed, try again.</p>}
      </div>
      {file && (
        <button
          className="bg-blue-500 px-4 py-2 rounded mr-2 no-underline"
          onClick={handleUpload}
        >
          Upload {file.name}
        </button>
      )}
    </div>
  );
}
