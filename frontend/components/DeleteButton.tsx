"use client";
import { deleteIngestion } from "@/lib/api";
import { useRouter } from "next/navigation";

// this is a prop type definition
interface Props {
  id: number;
}

export default function DeleteButton({ id }: Props) {
  const router = useRouter();

  async function handleDelete() {
    await deleteIngestion(id);
    router.refresh();
  }

  return (
    <button
      className="bg-red-500 text-white px-4 py-2 rounded mr-2 no-underline"
      onClick={handleDelete}
    >
      Delete
    </button>
  );
}
