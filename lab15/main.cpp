#include <iostream>
#include<string>
#include <vector>

class Tree
{
public:
	int value;
	Tree* p;
	Tree* l;
	Tree* r;
	std::string string;

	Tree(const int v, Tree* parent)
	{
		value = v;
		p = parent;
	}

	Tree()
	{

	}

	Tree(std::string str)
	{
		string = str;
	}


	void add(const int v)
	{
		if (v > value)
		{
			if (r == nullptr)
			{
				r = new Tree(v, this);
			}
			else
			{
				r->add(v);
			}
		}
		else
		{
			if (l == nullptr)
			{
				l = new Tree(v, this);
			}
			else
			{
				l->add(v);
			}
		}
	}


	std::string toString(int value)
	{
		std::string result;

		if (value > 9)
		{
			result += char(value / 10 + 48);
			result += char(value % 10 + 48);
		}
		else
		{
			result += char(value + 48);
		}

		return result;
	}

	void print(Tree* tree)
	{
		string += toString(tree->value);
		if (tree->l != nullptr || tree->r != nullptr)
		{
			string += '(';
			if (tree->l != nullptr)
			{
				print(tree->l);
			}
			string += ',';
			if (tree->r != nullptr)
			{
				print(tree->r);
			}
			string += ')';
		}

	}


	void Print()
	{
		print(this);
	}

	bool isDigital(const char elem)
	{
		return (elem >= '0' && elem <= '9') ? true : false;
	}

	Tree parse(std::string str)
	{
		Tree result;
		int index;
		if (isDigital(str[0]) && isDigital(str[1]))
		{
			int val = (str[0] - 48) * 10 + str[1] - 48;
			result.value = val;
			index = 2;
		}
		else if (isDigital(str[0]) && !isDigital(str[1]))
		{
			int val = str[0] - 48;
			result.value = val;
			index = 1;
		}


		for (int i = index; i < str.size() - 1;)
		{
			if (isDigital(str[i]) && isDigital(str[i + 1]))
			{
				int value = (str[i] - 48) * 10 + str[i + 1] - 48;
				result.add(value);
				i += 2;
			}
			else if (isDigital(str[i]) && !isDigital(str[i + 1]))
			{
				int value = str[i] - 48;
				result.add(value);
				i++;
			}
			else
			{
				i++;
			}
		}

		return result;
	}
};

void direct(std::vector <int>& v, const Tree* tree)
{
	if (tree != nullptr)
	{
		v.push_back(tree->value);
		direct(v, tree->l);
		direct(v, tree->r);
	}
}


void center(std::vector<int>& v, const Tree* tree)
{
	if (tree != nullptr)
	{
		center(v, tree->l);
		v.push_back(tree->value);
		center(v, tree->r);
	}
}


void reverse(std::vector<int>& v, const Tree* tree)
{
	if (tree != nullptr)
	{
		reverse(v, tree->l);
		reverse(v, tree->r);
		v.push_back(tree->value);
	}
}


void main()
{
	std::vector <int> dV;
	std::vector <int> cV;
	std::vector <int> rV;
	int maxElem;
	std::string str = "8(3(1,6(4,5)),10(,13(12,)))";
	Tree tree;
	tree = tree.parse(str);
	Tree newTree = tree;
	newTree.Print();

	direct(dV, &newTree);
	center(cV, &newTree);
	reverse(rV, &newTree);

	for (auto& value : rV)
	{
		std::cout << value << "\t";
	}
}
