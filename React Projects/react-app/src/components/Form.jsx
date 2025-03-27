import { useState, useEffect } from 'react'
import './form.css'

function Form(){

    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');

    return (
        <>
        <h2>General Information</h2>
        <div className='gen-info'>
            <div>
            <form>
                <label>
                    Name:
                    <input 
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)} />
                </label>
            <p>{name}</p>
            </form>
            </div>
            <div>
                <form>
                    <label>
                        E-Mail:
                        <input  
                            type='text'
                            value={email}
                            onChange={(e) => setEmail(e.target.value)} />
                    </label>
                    <p>{email}</p>
                </form>
            </div>
            <div>
                <form>
                    <label>
                        Phone:
                        <input  
                            type='text'
                            value={phone}
                            onChange={(e) => setPhone(e.target.value)} />
                    </label>
                    <p>{phone}</p>
                </form>
            </div>
        
      </div>
      </>
    )
}

export default Form;