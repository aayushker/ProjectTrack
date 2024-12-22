"use client";
import { useEffect, useState } from "react";
import { fetchProjects, acceptProject, updateProgress } from "./services/api";

interface Project {
  id: number;
  title: string;
  description: string;
  status: string;
}

export default function Home() {
  const [projects, setProjects] = useState<Project[]>([]);

  useEffect(() => {
    fetchProjects().then(({ data }) => setProjects(data));
  }, []);

  const handleAccept = (id: number) => {
    acceptProject(id).then(() => alert("Project accepted!"));
  };

  const handleUpdate = (id: number) => {
    const completion = prompt("Enter completion percentage (0-100):");
    updateProgress(id, { completion_percentage: completion }).then(() =>
      alert("Progress updated!")
    );
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Projects</h1>
      {projects.map((project) => (
        <div key={project.id} className="border p-4 mb-2">
          <h2>{project.title}</h2>
          <p>{project.description}</p>
          <p>Status: {project.status}</p>
          <button
            className="bg-blue-500 text-white px-2 py-1"
            onClick={() => handleAccept(project.id)}
          >
            Accept
          </button>
          <button
            className="bg-green-500 text-white px-2 py-1 ml-2"
            onClick={() => handleUpdate(project.id)}
          >
            Update Progress
          </button>
        </div>
      ))}
    </div>
  );
}
