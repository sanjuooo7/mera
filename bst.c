#include <stdio.h>
#include <stdlib.h>

struct Node 
{
    int key;
    struct Node* left;
    struct Node* right;
};
struct Node* createNode(int key) 
{
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->key = key;
    newNode->left = newNode->right = NULL;
    return newNode;
}
struct Node* insert(struct Node* root, int key) 
{
    if (root == NULL) 
    {
        return createNode(key);
    }

    if (key < root->key) 
    {
        root->left = insert(root->left, key);
	} 
	else if (key > root->key) 
	{
        root->right = insert(root->right, key);
    }
    else
    {
    printf("unable to insert key.%d already exists in the tree\n",key);
    }
    return root;
}
struct Node* findMin(struct Node* root) 
{
    while (root->left != NULL) 
    {
        root = root->left;
    }
    return root;
}
struct Node* deleteNode(struct Node* root, int key) 
{
    if (root == NULL) 
    {
        return root;
    }

    if (key < root->key) 
    {
        root->left = deleteNode(root->left, key);
    } 
    else if (key > root->key) 
    {
        root->right = deleteNode(root->right, key);
    }
     else 
     {
        if (root->left == NULL) 
        {
            struct Node* temp = root->right;
            free(root);
            return temp;
        }
        	else if (root->right == NULL) 
        	{
           	struct Node* temp = root->left;
           	free(root);
            	return temp;
        	}
        
        struct Node* temp = findMin(root->right);
        root->key = temp->key;
        root->right = deleteNode(root->right, temp->key);
    }
    return root;
}
struct Node* search(struct Node* root, int key) 
{
    if (root == NULL || root->key == key) 
    {
        return root;
    }

    if (key < root->key) 
    {
        return search(root->left, key);
    }
    return search(root->right, key);
}
void inorderTraversal(struct Node* root) 
{
    if (root != NULL) 
    {
        inorderTraversal(root->left);
        printf("%d ", root->key);
        inorderTraversal(root->right);
    }
}
void preorderTraversal(struct Node* root) 
{
    if (root != NULL)
    {
        printf("%d ", root->key);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
    }
}
void postorderTraversal(struct Node* root) 
{
    if (root != NULL) 
    {
        postorderTraversal(root->left);
        postorderTraversal(root->right);
        printf("%d ", root->key);
    }
}
int main() 
{
    struct Node* root = NULL;
    int n, key, deleteKey, insertKey, searchKey;
    int choice;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    printf("Enter the elements:\n");
    for (int i = 0; i < n; ++i) 
    {
        scanf("%d", &key);
        root = insert(root, key);
    }   
    while(1)
    {

		printf("Choose operation:\n");
    		printf("1. Inorder Traversal\n2. Preorder Traversal\n3. Postorder Traversal\n4. Delete Node\n5. Insert Node\n6. Search Node\n0. Exit\n");
    		scanf("%d", &choice);
    		switch (choice) 
    		{
       		case 1:
            		printf("Inorder traversal: ");
            		inorderTraversal(root);
            		            		printf("\n");
            		break;
        		case 2:
            		printf("Preorder traversal: ");
            		preorderTraversal(root);
            		            		printf("\n");
            		break;
        case 3:
           		printf("Postorder traversal: ");
            		postorderTraversal(root);
            		            		printf("\n");
            		break;
        case 4:
            		printf("Enter the key to delete: ");
            		scanf("%d", &deleteKey);
            		root = deleteNode(root, deleteKey);
            		printf("Inorder traversal after deletion: ");
                	printf("\n");
            		inorderTraversal(root);
            		break;
        case 5:
            		printf("Enter the key to insert: ");
            		scanf("%d", &insertKey);
            		root = insert(root, insertKey);
            		printf("Inorder traversal after insertion: ");
            		printf("\n");
           		inorderTraversal(root);
            		break;
        case 6:
            		printf("Enter the key to search: ");
            		scanf("%d", &searchKey);
            		struct Node* searchResult = search(root, searchKey);
            		if (searchResult != NULL) 
            		{
                		printf("Node with key %d found in the tree.\n", searchKey);
            		} 
            		else 
            		{
                		printf("Node with key %d not found in the tree.\n", searchKey);
            		}
            		break;
        case 0:
            		exit(0);
       default:
                printf("Invalid choice\n");
    		}
    }
    return 0;
}
