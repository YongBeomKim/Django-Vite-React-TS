import { Suspense } from 'react'
import Navbar from './Components/Navbar';
import Home from './Pages/Home';


function App() {
  return (
    <>
      <Suspense fallback={<div>Loading ...</div>}>
        <section>
          <Navbar />
        </section>
        <section>
          <Home />
        </section>
      </Suspense>
    </>
  )
}

export default App
