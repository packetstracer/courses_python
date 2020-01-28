import unittest
import os


def annalyze_text(filename):
  """ Calcula el número de líneas y palabras en un fichero

  Args:
    filename: el nombre del fichero a procesar

  Raises:
    IOError: if ``filename`` does not exist or cannot be opened

  Returns: una tupla con el número de líneas y el número de caracteres del fichero
  """
  with open(filename, 'rt') as f:
    lines = f.readlines()

  with open(filename, 'rt') as f:
    chars = sum(len(line) for line in f)

  return (len(lines), chars)


class TextAnalysisTests(unittest.TestCase):
  """Tests for analyze_text function."""

  def setUp(self):
    """Fixture to create a test file (this method setUp is always executed before each test)"""
    self.filename = 'text_analysis_test_file.txt'
    self.lines_number = 3
    self.chars_number = 111

    with open(self.filename, 'wt', encoding = 'utf-8') as f:
      f.write('Lineas del fichero de texto de pruebas\n'
              'que nos va a servir para contar\n'
              'las palabras que acabamos de introducir.')


  def tearDown(self):
    """Fixture that deletes the test files created (this method is always executed after each test)"""
    try:
      os.remove(self.filename)
    except:
      pass


  def test_function_runs(self):
    """Basic test that checks if runs (test functions must be prefixed with test_)"""
    annalyze_text(self.filename)


  def test_line_count(self):
    """Check that the line count is correct"""
    (line_count, _) = annalyze_text(self.filename)

    self.assertEqual(line_count, self.lines_number)


  def test_character_count(self):
    """Check that the characer count is correct"""
    (_, character_count) = annalyze_text(self.filename)

    self.assertEqual(character_count, self.chars_number)


  def test_no_such_file(self):
    """Check that raises IOError exception if file does not exist"""
    with self.assertRaises(IOError):
      annalyze_text('non_existent_file.txt')


  def test_file_not_deleted(self):
    """Check that does not delete the passed file"""
    annalyze_text(self.filename)
    self.assertTrue(os.path.exists(self.filename))



if __name__ == '__main__':
  # run all the test functions (test_*())
  unittest.main()