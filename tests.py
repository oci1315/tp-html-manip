from csudoci.html.parser import html_to_tree
from csudoci.html.manip import get_links
from csudoci.html.htmltree import *

from tp_html import *

import unittest


class ManipTestCase(unittest.TestCase):
    
    def setUp(self):
        with open('test.html', mode='r', encoding='utf-8') as fd:
            self.test_html = fd.read()
            self.root = html_to_tree(self.test_html)

    def assertTreeEqual(self, t1, t2):
        if isinstance(t1, T):
            self.assertIsInstance(t2, T)
        else:
            self.assertEqual(t1.tag, t2.tag)
        
        self.assertEqual(len(t1.children), len(t2.children))
        
        for i in range(len(t1.children)):
            self.assertTreeEqual(t1.children[i], t2.children[i])
            
    def assertHtmlEquiv(self, html1, html2):
        self.assertTreeEqual(html_to_tree(html1), html_to_tree(html2))

    def assertTreeEquivHtml(self, tree, html):
        self.assertTreeEqual(tree, html_to_tree(html))


class TestGetElements(ManipTestCase):

    def test_match_with_get_links(self):
    
        # get_elements devrait donner le même résultat que si on appelle get_links
        # en restreignant les éléments à a
        self.assertEqual(
            get_elements(self.root, ['a']),
            get_links(self.root)
        )
        
    def test_correct_first_header_text(self):
        
        # devrait renvoyer la liste de tous les titres ==> table des matières
        headers = get_elements(self.root, ['h1', 'h2', 'h3'])
        self.assertTreeEquivHtml(
            headers[0],
            '<h1>Document de test</h1>'
        )
        
    def test_correct_header_list(self):
        
        headers = get_elements(self.root, ['h1', 'h2', 'h3'])
        self.assertEqual(
            [h.tag for h in headers],
            ['h1', 'h2', 'h2', 'h3', 'h3', 'h3', 'h2', 'h3', ]
        )
        
        headers = get_elements(self.root, ['h1', 'h2',])
        self.assertEqual(
            [h.tag for h in headers],
            ['h1', 'h2', 'h2', 'h2', ]
        )
        
    def test_no_selectors(self):
        
        self.assertEqual(
            get_elements(self.root, []),
            []
        )
        

class TestTableMatieres(ManipTestCase):
    
    def test_default_level(self):
        self.assertEqual(
            table_matieres(self.root),
            table_matieres(self.root, level=2)
        )
        
    def test_from_file(self):
        headers = table_matieres(self.root, level=3)
        self.assertEqual(
            [h.tag for h in headers],
            ['h1', 'h2', 'h2', 'h3', 'h3', 'h3', 'h2', 'h3', ]
        )
        
    
class TextRemoveLinks(ManipTestCase):

    def assertLinksRemoved(self, html, html_without_links):
        tree1 = remove_links(html_to_tree(html))
        tree2 = html_to_tree(html_without_links)
        
        self.assertTreeEqual(
            tree1,
            tree2
        )

    def test_remove_root_link(self):
        self.assertLinksRemoved('''
            <a href="http://www.google.com">
                Texte du lien
            </a>
            ''',
            '''<span>Texte du lien</span>'''
        )
        
    def test_a_with_many_children(self):
        self.assertLinksRemoved('''
            <div>
                <a href="http://www.google.com">
                    <span>T1</span>
                    Texte du lien
                    <span>T2</span>
                </a>
            </div>''',
            '''<div><span>T1</span>Texte du lien<span>T2</span></div>'''
        )
        
    def test_empty_html(self):
        self.assertLinksRemoved('<div></div>', '<div></div>')
        

if __name__ == '__main__':
    unittest.main()