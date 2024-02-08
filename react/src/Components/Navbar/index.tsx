
/* Navbar */
const Navbar = () => {
  return (
    <div className="text-center bg-white shadow">
      <nav className="flex flex-col py-4 px-6 
        text-grey-darkest w-full no-underline
        hover:text-blue-dark
        sm:flex-row sm:text-left sm:justify-between sm:items-baseline">
        <div className="mb-2 sm:mb-0">
          <a href="#" className="text-2xl">Home</a>
        </div>
        <div className="text-lg">
          <a href="#" className="ml-2">User</a>
          <a href="#" className="ml-2">Two</a>
          <a href="#" className="ml-2">Three</a>
        </div>
      </nav>
    </div>
  )
}

export default Navbar