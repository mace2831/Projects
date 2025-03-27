import {useState} from 'react'

function WorkExperienceList(){
    
    const [workExperience, setWorkExperience] = useState([
        {
            id: 1,
            company: 'Company',
            title: 'Title',
            start: 'Start',
            end: 'End',
            description: 'Description'
        },
        {
            id: 1,
            company: 'Company',
            title: 'Title',
            start: 'Start',
            end: 'End',
            description: 'Description'
        }
    ])

    const addExperience = (newExperience) => {
        setWorkExperience([
            ...workExperience, {
                ...newExperience, id: workExperience.id +1
            }

        ]);
    }

    return(
        <div>
            <h2>Work Experience</h2>
            {workExperience.map((exp) => (
                <WorkExperience
                    key={exp.id}
                    company={exp.company}
                    title={exp.title}
                    start={exp.start}
                    end={exp.end}
                    description={exp.description} />
            ))}
        </div>
    );

}


function WorkExperience({company, title, start, end, description}){

    

    return(
        
        <div>
            
                <>
                <p>{company}</p>
                <p>{title}</p>
                <p>{start}</p>
                <p>{end}</p>
                <p>{description}</p>
                </>
            
        </div>
        
    );
}

export default WorkExperienceList;