{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello World\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n",
      "World!\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello\\nWorld!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World!\n"
     ]
    }
   ],
   "source": [
    " print('Hello World!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(1.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bool(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "Numbers=\"0123456\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'0246'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Numbers[::2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"0123456\".find('1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3 + 2 * 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "name = 'Lizz'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Li\n"
     ]
    }
   ],
   "source": [
    "print(name[0:2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'12'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'1'+'2'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#------------------ Part #2 -----------------------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Lists and Tuples \n",
    "#Sets\n",
    "#Dictionaries "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "A=(0,1,2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "B=[\"a\",\"b\",\"c\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['b', 'c']"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "B[1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "#sets\n",
    "S={'A','B','C'}\n",
    "\n",
    "U={'A','Z','C'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'A', 'B', 'C', 'Z'}"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "U.union(S)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'A', 'C'}"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "S.intersection(U)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "D={'a':0,'b':1,'c':2}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values([0, 1, 2])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "D.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "L=['1','4','5']\n",
    "L.append(['a','b'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['1', '4', '5', ['a', 'b']]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['1', '4', '5', ['a', 'b']]\n"
     ]
    }
   ],
   "source": [
    "print(L)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "Dict = {\"A\": 1, \"B\": \"2\", \"C\": [3,3,3], \"D\" :( 4,4,4), 'E': 5, 'F' : 6}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4, 4, 4)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Dict [\"D\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "#------------------------Condiciones y ramificacion---------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "i=1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "i!=0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "A=[3,4,5]\n",
    "\n",
    "for a in A:\n",
    "    print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n"
     ]
    }
   ],
   "source": [
    "a=1\n",
    "\n",
    "def add(b):\n",
    "\n",
    "    return a+b\n",
    "\n",
    "c=add(10)\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "def f(*x):\n",
    "\n",
    "    return sum(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "make=\"Honda\"\n",
    "\n",
    "model=\"Accord\"\n",
    "\n",
    "color=\"blue\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n",
      "22\n",
      "33\n"
     ]
    }
   ],
   "source": [
    "A=['1','2','3']\n",
    "\n",
    "for a in A:\n",
    "\n",
    "    print(2*a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "A=['31','2','3']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['2', '3', '31']\n"
     ]
    }
   ],
   "source": [
    "A.sort()\n",
    "print(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "C={'a':1,'b':2}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['a', 'b'])"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "C.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values([1, 2])"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "C.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "# ------- Leer docs----------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "# f.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Pandas Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>show_id</th>\n",
       "      <th>type</th>\n",
       "      <th>title</th>\n",
       "      <th>director</th>\n",
       "      <th>cast</th>\n",
       "      <th>country</th>\n",
       "      <th>date_added</th>\n",
       "      <th>release_year</th>\n",
       "      <th>rating</th>\n",
       "      <th>duration</th>\n",
       "      <th>listed_in</th>\n",
       "      <th>description</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>s1</td>\n",
       "      <td>TV Show</td>\n",
       "      <td>3%</td>\n",
       "      <td>NaN</td>\n",
       "      <td>João Miguel, Bianca Comparato, Michel Gomes, R...</td>\n",
       "      <td>Brazil</td>\n",
       "      <td>August 14, 2020</td>\n",
       "      <td>2020</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>4 Seasons</td>\n",
       "      <td>International TV Shows, TV Dramas, TV Sci-Fi &amp;...</td>\n",
       "      <td>In a future where the elite inhabit an island ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>s2</td>\n",
       "      <td>Movie</td>\n",
       "      <td>7:19</td>\n",
       "      <td>Jorge Michel Grau</td>\n",
       "      <td>Demián Bichir, Héctor Bonilla, Oscar Serrano, ...</td>\n",
       "      <td>Mexico</td>\n",
       "      <td>December 23, 2016</td>\n",
       "      <td>2016</td>\n",
       "      <td>TV-MA</td>\n",
       "      <td>93 min</td>\n",
       "      <td>Dramas, International Movies</td>\n",
       "      <td>After a devastating earthquake hits Mexico Cit...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>s3</td>\n",
       "      <td>Movie</td>\n",
       "      <td>23:59</td>\n",
       "      <td>Gilbert Chan</td>\n",
       "      <td>Tedd Chan, Stella Chung, Henley Hii, Lawrence ...</td>\n",
       "      <td>Singapore</td>\n",
       "      <td>December 20, 2018</td>\n",
       "      <td>2011</td>\n",
       "      <td>R</td>\n",
       "      <td>78 min</td>\n",
       "      <td>Horror Movies, International Movies</td>\n",
       "      <td>When an army recruit is found dead, his fellow...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>s4</td>\n",
       "      <td>Movie</td>\n",
       "      <td>9</td>\n",
       "      <td>Shane Acker</td>\n",
       "      <td>Elijah Wood, John C. Reilly, Jennifer Connelly...</td>\n",
       "      <td>United States</td>\n",
       "      <td>November 16, 2017</td>\n",
       "      <td>2009</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>80 min</td>\n",
       "      <td>Action &amp; Adventure, Independent Movies, Sci-Fi...</td>\n",
       "      <td>In a postapocalyptic world, rag-doll robots hi...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>s5</td>\n",
       "      <td>Movie</td>\n",
       "      <td>21</td>\n",
       "      <td>Robert Luketic</td>\n",
       "      <td>Jim Sturgess, Kevin Spacey, Kate Bosworth, Aar...</td>\n",
       "      <td>United States</td>\n",
       "      <td>January 1, 2020</td>\n",
       "      <td>2008</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>123 min</td>\n",
       "      <td>Dramas</td>\n",
       "      <td>A brilliant group of students become card-coun...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  show_id     type  title           director  \\\n",
       "0      s1  TV Show     3%                NaN   \n",
       "1      s2    Movie   7:19  Jorge Michel Grau   \n",
       "2      s3    Movie  23:59       Gilbert Chan   \n",
       "3      s4    Movie      9        Shane Acker   \n",
       "4      s5    Movie     21     Robert Luketic   \n",
       "\n",
       "                                                cast        country  \\\n",
       "0  João Miguel, Bianca Comparato, Michel Gomes, R...         Brazil   \n",
       "1  Demián Bichir, Héctor Bonilla, Oscar Serrano, ...         Mexico   \n",
       "2  Tedd Chan, Stella Chung, Henley Hii, Lawrence ...      Singapore   \n",
       "3  Elijah Wood, John C. Reilly, Jennifer Connelly...  United States   \n",
       "4  Jim Sturgess, Kevin Spacey, Kate Bosworth, Aar...  United States   \n",
       "\n",
       "          date_added  release_year rating   duration  \\\n",
       "0    August 14, 2020          2020  TV-MA  4 Seasons   \n",
       "1  December 23, 2016          2016  TV-MA     93 min   \n",
       "2  December 20, 2018          2011      R     78 min   \n",
       "3  November 16, 2017          2009  PG-13     80 min   \n",
       "4    January 1, 2020          2008  PG-13    123 min   \n",
       "\n",
       "                                           listed_in  \\\n",
       "0  International TV Shows, TV Dramas, TV Sci-Fi &...   \n",
       "1                       Dramas, International Movies   \n",
       "2                Horror Movies, International Movies   \n",
       "3  Action & Adventure, Independent Movies, Sci-Fi...   \n",
       "4                                             Dramas   \n",
       "\n",
       "                                         description  \n",
       "0  In a future where the elite inhabit an island ...  \n",
       "1  After a devastating earthquake hits Mexico Cit...  \n",
       "2  When an army recruit is found dead, his fellow...  \n",
       "3  In a postapocalyptic world, rag-doll robots hi...  \n",
       "4  A brilliant group of students become card-coun...  "
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "csv_path='netflix.csv'\n",
    "df=pd.read_csv(csv_path)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "songs={'Album': ['Thriller','Back in Black','The Dar Side of the Moon','The Bodyguard'],\n",
    "       'Released':[1946,2005,2015,2018], \n",
    "       'Length':['00:34:25','01:24:24','01:00:00','00:42:00']}\n",
    "\n",
    "frame_songs=pd.DataFrame(songs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>a</th>\n",
       "      <th>b</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>11</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>21</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>31</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    a   b\n",
       "0  11  21\n",
       "1  21  22\n",
       "2  31  23"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as banana\n",
    "\n",
    "df=banana.DataFrame({'a':[11,21,31],'b':[21,22,23]})\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     True\n",
       "1    False\n",
       "2     True\n",
       "Name: a, dtype: bool"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['a']==1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('new_songes.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [],
   "source": [
    "#---------------------APIS--------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "#------------------Numpy----------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "a=np.array([0,1,2,3,4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int32')"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a:np.array([0,1,2,3,4])\n",
    "type(a)\n",
    "a.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.ndim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "b=np.array([3.3,61.5,7.3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "numpy.ndarray"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1, -1])"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.array([1,-1])*np.array([1,1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.dot(np.array([1,-1]),np.array([1,1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=np.linspace(0,2*np.pi,100)\n",
    "y=np.sin(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x236ef418550>]"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "plt.plot(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2]\n",
      " [3 4]\n",
      " [5 6]\n",
      " [7 8]]\n"
     ]
    }
   ],
   "source": [
    "A=np.array([[1,2],[3,4],[5,6],[7,8]])\n",
    "print(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [],
   "source": [
    "A=np.array([[1,2],[3,4],[5,6],[7,8]])\n",
    "B=np.array([[1,2,3],[4,5,6],[7,8,9]])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 0, 0])"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=np.array([0,1,0,1,0])\n",
    "\n",
    "b=np.array([1,0,1,0,1])\n",
    "\n",
    "a*b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=np.array([0,1])\n",
    "\n",
    "b=np.array([1,0])\n",
    "\n",
    "np.dot(a,b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([11, 11, 11, 11, 11])"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=np.array([1,1,1,1,1])\n",
    "\n",
    "a+10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [],
   "source": [
    "#---Examen------------------\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [],
   "source": [
    "a=True?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a=True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(3.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'246'"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A='1234567'\n",
    "A[1::2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Name=\"Michael Jackson\" \n",
    "Name.find('el')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'12'"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A='1'\n",
    "B='2'\n",
    "A+B\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C'"
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tuple1=(\"A\",\"B\",\"C\" )\n",
    "tuple1[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[21, 22]"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A=((11,12),[21,22])\n",
    "A[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A=((11,12),[21,22])\n",
    "A[0][1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['1', '2', '3', '4']"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'1,2,3,4'.split(',')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 'a', 2, 1, 'd']"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A=[1,'a']\n",
    "B=[2,1,'d']\n",
    "A+B"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 'a'}\n"
     ]
    }
   ],
   "source": [
    "a=set(A)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [],
   "source": [
    "V={'A','B'}\n",
    "V.add('C')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'A', 'B', 'C'}\n"
     ]
    }
   ],
   "source": [
    "print(V)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [],
   "source": [
    "V={'A','B','C' }\n",
    "V.add('C')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'A', 'B', 'C'}\n"
     ]
    }
   ],
   "source": [
    "print(V)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "for n in range(3):\n",
    "\n",
    "    print(n+1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n",
      "22\n",
      "33\n"
     ]
    }
   ],
   "source": [
    "A=['1','2','3']\n",
    "\n",
    "for a in A:\n",
    "\n",
    "    print(2*a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1'"
      ]
     },
     "execution_count": 152,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def Add(x,y):\n",
    "\n",
    "    z=y+x\n",
    "\n",
    "    return(y)\n",
    "Add('1','1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Points(object):\n",
    "\n",
    "    def __init__(self,x,y):\n",
    "\n",
    "        self.x=x\n",
    "\n",
    "        self.y=y\n",
    "\n",
    "    def print_point(self):\n",
    "\n",
    "        print('x=',self.x,'y=',self.y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x= 1  y= 2\n"
     ]
    }
   ],
   "source": [
    "class Points(object):\n",
    "\n",
    "    def __init__(self,x,y):\n",
    "\n",
    "        self.x=x\n",
    "\n",
    "        self.y=y\n",
    "\n",
    "    def print_point(self):\n",
    "\n",
    "        print('x=',self.x,' y=',self.y)\n",
    "\n",
    "p1=Points(1,2)\n",
    "\n",
    "p1.print_point()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x= 2  y= 2\n"
     ]
    }
   ],
   "source": [
    "class Points(object):\n",
    "\n",
    "    def __init__(self,x,y):\n",
    "\n",
    "        self.x=x\n",
    "\n",
    "        self.y=y\n",
    "\n",
    "    def print_point(self):\n",
    "\n",
    "        print('x=',self.x,' y=',self.y)\n",
    "\n",
    "p2=Points(1,2)\n",
    "\n",
    "p2.x=2\n",
    "\n",
    "p2.print_point()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
