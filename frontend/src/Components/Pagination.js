import React from 'react';

var number1 = 1

const Pagination = ({ postsPerPage, totalPosts, paginate }) => {
  const pageNumbers = [];
  const pagactual = (number, opcion) => {
    console.log("number1:",number1)
    console.log("number:",number)
    if (opcion === 0) {
      number1 = number
      paginate(number)

    }
    if (opcion === 1) {
        // Avanzar
      if (number1 > totalPosts / 10) {
        number1 = number1
        console.log(number1)

      } else {
        paginate(number1 + 1)
        number1 = number1 + 1
        console.log(number1)
      }
    }
    if (opcion === 2) {
      if (number1 > 1){
        paginate(number1-1)
        number1 = number1-1
      }

    }
  }



  for (let i = 1; i <= Math.ceil(totalPosts / postsPerPage); i++) {
    pageNumbers.push(i);
  }

  return (
    <nav>
      <ul className='pagination pagination justify-content-end'>
        <li className="page-item">
          <a className="page-link" onClick={() => pagactual(number1, 2)}>Previous</a>
        </li>
        {pageNumbers.map(number => (
          <li key={number} className='page-item'>
            <a onClick={() => pagactual(number, 0)} className='page-link' >
              {number}
            </a>
          </li>
        ))}
        <li className="page-item">
          <a className="page-link" onClick={() => pagactual(number1, 1)}>Next</a>
        </li>
      </ul>
    </nav>
  );
};

export default Pagination;