import { Button } from "@/components/ui/button"
import { useState } from 'react'

export default function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <Button onClick={() => setCount(count + 1)}>Count: {count}</Button>
    </div>
  )
}
