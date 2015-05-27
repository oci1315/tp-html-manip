from csudoci.html.parser import HTMLTreeParser, html_to_tree
from csudoci.html.htmltree import Div, Span, T, E

def get_elements(tree, selectors):
    '''
    
    Filtre l'arbre et ne renvoie que les éléments dont la balise figure dans la liste
    ``selectors``. Ce sont des sous-arbres complets qui sont renvoyés puisque l'éléments
    racine fait référence à tout le sous-arbre.
    
    '''
    
    elements = []
    root = tree
    
    if root.tag in selectors:
        elements.append(tree)
    else:
        for c in tree.children:
            elements += get_elements(c, selectors)

    return elements
    
    
def table_matieres(root, level=2):
    hlevels = ['h' + str(lev+1) for lev in range(level)]
    return Div() > get_elements(root, hlevels)
    
    
    
def remove_links(root):
    
    for child in root.children:
        remove_links(child)
        
    if isinstance(root, T):
        return root
        
    if root.tag == 'a':
        if root.parent:
            # aller dans le parent et remplacer l'élément courant par ses enfants
            siblings = root.parent.children
            index = siblings.index(root)
            siblings[index:index+1] = root.children
            root.parent.children = siblings
            root.parent = None
            
        else:
            span = Span()
            span > root.children
            return span
        
    return root
    

if __name__ == '__main__':
    pass