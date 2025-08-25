import React, { useRef, useState } from 'react'



const App = () => {
  const [todo, setToDo] = useState("")
  const [todos, setToDos]=useState([])
  const handleClick= ()=>{
    if (!todo.trim()) return
    setToDos([...todos,todo])
    setToDo("")
    
  }
  const addToDo=(e)=>{
    setToDo(e.target.value)
  }
  console.log("todo is", todo)
  console.log("todos",todos)
  const handleUpdate=(index)=>{
    setToDo(todos[index])
    const filterd=()=>todos.filter((_,i)=>i !=index)
    setToDos(filterd)
    
    
    
  }
  const handleDel=(index)=>{
  
  const   deleted=todos.filter((_,i)=>
      i !=index
     
)  
     setToDos(deleted)
  }
  return (
  <div>
    <input placeholder="enter to-do" onChange={addToDo}   value={todo} name="to-do">
    </input>
     <button className="btn" onClick={handleClick}>
      Add
     
    </button>
   
   
    <ul>
        {todos.map((item, index) => (
          <li key={index}>{item}
          
            <button className="btn" onClick={()=>handleUpdate(index)}>
      update
     
    </button>
       <button className="btn" onClick={()=>handleDel(index)}>
   delete
     
    </button>
          </li>
        ))}
     
      
      </ul>
  </div>
    
   
  )
}


export default App
