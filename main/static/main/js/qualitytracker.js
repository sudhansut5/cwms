function addRow() {
    const table = document.querySelector('.table-bordered');
    const row = table.insertRow(-1);
  
    const fatalNonFatal = row.insertCell(0);
    const questions = row.insertCell(1);
    const category = row.insertCell(2);
    const checkpointsQuestions = row.insertCell(3);
    const auditorGuidelines = row.insertCell(4);
    const score = row.insertCell(5);
    const result = row.insertCell(6);
    const comments = row.insertCell(7);
  
    fatalNonFatal.textContent = 'non-fatal';
    questions.textContent = 'another question';
    category.textContent = 'another category';
    checkpointsQuestions.textContent = 'another checkpoint/question';
    auditorGuidelines.textContent = 'another auditor guideline';
    score.textContent = '8';
    result.textContent = 'pass';
    comments.textContent = 'another comment';
  }
