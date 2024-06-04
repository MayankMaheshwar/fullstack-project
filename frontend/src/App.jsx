import { useEffect, useState } from 'react'
import ContactList from './ContactList'
import ContactForm from './ContactForm'

function App() {
  const [contacts, setContacts] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);


  const closeModal = () => {
    setIsModalOpen(false);
  }

  const openModal = () => {
    if (!isModalOpen) {
      setIsModalOpen(true);
    }
  }
  useEffect(() => {
    fetchContacts();
  },[])
  const fetchContacts = async () => {
    const response = await fetch('http://127.0.0.1:5000/contacts')
    console.log(response,"sdf")
    const data = await response.json()

    setContacts(data.contacts)
    console.log(data.contacts)
}

console.log(contacts);
return <> <ContactList contacts={contacts} />

{isModalOpen && <div className="modal">}
<ContactForm />
</>


