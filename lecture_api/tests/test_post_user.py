from lecture_api.pages.page_book_store_users import PageBookStoreUsers


class TestCreateUser:

    user_id = None

    def test_create_user(self):
        page = PageBookStoreUsers()
        user = page.create_user('Vasua3', 'P@ssw0rd')
        self.user_id = user.get('id')

    def test_delete_user(self):
        page = PageBookStoreUsers()
        user_id = page.create_user('Vasua9', 'P@ssw0rd').get('id')
        page.delete_user(sudy_pyshy_ID=user_id)

