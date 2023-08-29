#include <Python.h>
#include <floatobject.h>

/**
 * print_python_list - prints py lists
 * @p: pointer
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *element = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
	}
}

/**
 * print_python_bytes - prints py bytes
 * @p: pointer
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	Py_ssize_t max_bytes = (size > 10) ? 10 : size;

	printf("  first %zd bytes: ", max_bytes);

	for (Py_ssize_t i = 0; i < max_bytes; i++)
	{
		printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
	}
	printf("\n");
}

/**
 * print_python_float - prints py float
 * @p: pointer
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %lf\n", PyFloat_AsDouble(p));
}
