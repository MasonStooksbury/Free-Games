# Japanese / 日本語 - Translations - Python 3 Only!
from seleniumbase import BaseCase
from seleniumbase import MasterQA


class セレニウムテストケース(BaseCase):  # noqa

    def __init__(self, *args, **kwargs):
        super(セレニウムテストケース, self).__init__(*args, **kwargs)
        self._language = "Japanese"

    def を開く(self, *args, **kwargs):
        # open(url)
        return self.open(*args, **kwargs)

    def URLを開く(self, *args, **kwargs):
        # open_url(url)
        return self.open_url(*args, **kwargs)

    def クリックして(self, *args, **kwargs):
        # click(selector)
        return self.click(*args, **kwargs)

    def ダブルクリックして(self, *args, **kwargs):
        # double_click(selector)
        return self.double_click(*args, **kwargs)

    def ゆっくりクリックして(self, *args, **kwargs):
        # slow_click(selector)
        return self.slow_click(*args, **kwargs)

    def リンクテキストをクリックします(self, *args, **kwargs):
        # click_link_text(link_text)
        return self.click_link_text(*args, **kwargs)

    def テキストを更新(self, *args, **kwargs):
        # update_text(selector, text)
        return self.update_text(*args, **kwargs)

    def 入力(self, *args, **kwargs):
        # type(selector, text)  # Same as update_text()
        return self.type(*args, **kwargs)

    def テキストを追加(self, *args, **kwargs):
        # add_text(selector, text)
        return self.add_text(*args, **kwargs)

    def テキストを取得(self, *args, **kwargs):
        # get_text(selector, text)
        return self.get_text(*args, **kwargs)

    def テキストを確認する(self, *args, **kwargs):
        # assert_text(text, selector)
        return self.assert_text(*args, **kwargs)

    def 正確なテキストを確認する(self, *args, **kwargs):
        # assert_exact_text(text, selector)
        return self.assert_exact_text(*args, **kwargs)

    def リンクテキストを確認する(self, *args, **kwargs):
        # assert_link_text(link_text)
        return self.assert_link_text(*args, **kwargs)

    def 要素を確認する(self, *args, **kwargs):
        # assert_element(selector)
        return self.assert_element(*args, **kwargs)

    def 要素が表示されていることを確認(self, *args, **kwargs):
        # assert_element_visible(selector)  # Same as self.assert_element()
        return self.assert_element_visible(*args, **kwargs)

    def 要素が表示されていないことを確認します(self, *args, **kwargs):
        # assert_element_not_visible(selector)
        return self.assert_element_not_visible(*args, **kwargs)

    def 要素が存在することを確認します(self, *args, **kwargs):
        # assert_element_present(selector)
        return self.assert_element_present(*args, **kwargs)

    def 要素が存在しないことを確認します(self, *args, **kwargs):
        # assert_element_absent(selector)
        return self.assert_element_absent(*args, **kwargs)

    def タイトルを確認(self, *args, **kwargs):
        # assert_title(title)
        return self.assert_title(*args, **kwargs)

    def タイトルを取得する(self, *args, **kwargs):
        # get_title()
        return self.get_title(*args, **kwargs)

    def 検証が正しい(self, *args, **kwargs):
        # assert_true(expr)
        return self.assert_true(*args, **kwargs)

    def 検証は偽です(self, *args, **kwargs):
        # assert_false(expr)
        return self.assert_false(*args, **kwargs)

    def 検証が等しい(self, *args, **kwargs):
        # assert_equal(first, second)
        return self.assert_equal(*args, **kwargs)

    def 検証が等しくない(self, *args, **kwargs):
        # assert_not_equal(first, second)
        return self.assert_not_equal(*args, **kwargs)

    def ページを更新する(self, *args, **kwargs):
        # refresh_page()
        return self.refresh_page(*args, **kwargs)

    def 現在のURLを取得(self, *args, **kwargs):
        # get_current_url()
        return self.get_current_url(*args, **kwargs)

    def ページのソースコードを取得する(self, *args, **kwargs):
        # get_page_source()
        return self.get_page_source(*args, **kwargs)

    def 戻る(self, *args, **kwargs):
        # go_back()
        return self.go_back(*args, **kwargs)

    def 進む(self, *args, **kwargs):
        # go_forward()
        return self.go_forward(*args, **kwargs)

    def テキストが表示されています(self, *args, **kwargs):
        # is_text_visible(text, selector="html")
        return self.is_text_visible(*args, **kwargs)

    def 要素は表示されますか(self, *args, **kwargs):
        # is_element_visible(selector)
        return self.is_element_visible(*args, **kwargs)

    def 要素が存在するかどうか(self, *args, **kwargs):
        # is_element_present(selector)
        return self.is_element_present(*args, **kwargs)

    def テキストを待つ(self, *args, **kwargs):
        # wait_for_text(text, selector)
        return self.wait_for_text(*args, **kwargs)

    def 要素を待つ(self, *args, **kwargs):
        # wait_for_element(selector)
        return self.wait_for_element(*args, **kwargs)

    def 要素が表示されるのを待ちます(self, *args, **kwargs):
        # wait_for_element_visible(selector)  # Same as wait_for_element()
        return self.wait_for_element_visible(*args, **kwargs)

    def 要素が表示されなくなるまで待ちます(self, *args, **kwargs):
        # wait_for_element_not_visible(selector)
        return self.wait_for_element_not_visible(*args, **kwargs)

    def 要素が存在するのを待つ(self, *args, **kwargs):
        # wait_for_element_present(selector)
        return self.wait_for_element_present(*args, **kwargs)

    def 要素が存在しないのを待つ(self, *args, **kwargs):
        # wait_for_element_absent(selector)
        return self.wait_for_element_absent(*args, **kwargs)

    def 眠る(self, *args, **kwargs):
        # sleep(seconds)
        return self.sleep(*args, **kwargs)

    def 待つ(self, *args, **kwargs):
        # wait(seconds)  # Same as sleep(seconds)
        return self.wait(*args, **kwargs)

    def を提出す(self, *args, **kwargs):
        # submit(selector)
        return self.submit(*args, **kwargs)

    def JSクリックして(self, *args, **kwargs):
        # js_click(selector)
        return self.js_click(*args, **kwargs)

    def JSテキストを更新(self, *args, **kwargs):
        # js_update_text(selector, text)
        return self.js_update_text(*args, **kwargs)

    def JS入力(self, *args, **kwargs):
        # js_type(selector, text)
        return self.js_type(*args, **kwargs)

    def HTMLをチェック(self, *args, **kwargs):
        # inspect_html()
        return self.inspect_html(*args, **kwargs)

    def スクリーンショットを保存(self, *args, **kwargs):
        # save_screenshot(name)
        return self.save_screenshot(*args, **kwargs)

    def ファイルを選択(self, *args, **kwargs):
        # choose_file(selector, file_path)
        return self.choose_file(*args, **kwargs)

    def スクリプトを実行する(self, *args, **kwargs):
        # execute_script(script)
        return self.execute_script(*args, **kwargs)

    def ブロック広告(self, *args, **kwargs):
        # ad_block()
        return self.ad_block(*args, **kwargs)

    def スキップ(self, *args, **kwargs):
        # skip(reason="")
        return self.skip(*args, **kwargs)

    def リンク切れを確認する(self, *args, **kwargs):
        # assert_no_404_errors()
        return self.assert_no_404_errors(*args, **kwargs)

    def JSエラーを確認する(self, *args, **kwargs):
        # assert_no_js_errors()
        return self.assert_no_js_errors(*args, **kwargs)

    def フレームに切り替え(self, *args, **kwargs):
        # switch_to_frame(frame)
        return self.switch_to_frame(*args, **kwargs)

    def デフォルトのコンテンツに切り替える(self, *args, **kwargs):
        # switch_to_default_content()
        return self.switch_to_default_content(*args, **kwargs)

    def 新しいウィンドウを開く(self, *args, **kwargs):
        # open_new_window()
        return self.open_new_window(*args, **kwargs)

    def ウィンドウに切り替え(self, *args, **kwargs):
        # switch_to_window(window)
        return self.switch_to_window(*args, **kwargs)

    def デフォルトのウィンドウに切り替える(self, *args, **kwargs):
        # switch_to_default_window()
        return self.switch_to_default_window(*args, **kwargs)

    def ウィンドウを最大化する(self, *args, **kwargs):
        # maximize_window()
        return self.maximize_window(*args, **kwargs)

    def ハイライト(self, *args, **kwargs):
        # highlight(selector)
        return self.highlight(*args, **kwargs)

    def ハイライトしてクリックして(self, *args, **kwargs):
        # highlight_click(selector)
        return self.highlight_click(*args, **kwargs)

    def スクロールして(self, *args, **kwargs):
        # scroll_to(selector)
        return self.scroll_to(*args, **kwargs)

    def 一番上までスクロール(self, *args, **kwargs):
        # scroll_to_top()
        return self.scroll_to_top(*args, **kwargs)

    def 一番下までスクロール(self, *args, **kwargs):
        # scroll_to_bottom()
        return self.scroll_to_bottom(*args, **kwargs)

    def 上にマウスを移動しクリック(self, *args, **kwargs):
        # hover_and_click(hover_selector, click_selector)
        return self.hover_and_click(*args, **kwargs)

    def 選択されていることを(self, *args, **kwargs):
        # is_selected(selector)
        return self.is_selected(*args, **kwargs)

    def 上矢印を押します(self, *args, **kwargs):
        # press_up_arrow(selector="html", times=1)
        return self.press_up_arrow(*args, **kwargs)

    def 下矢印を押します(self, *args, **kwargs):
        # press_down_arrow(selector="html", times=1)
        return self.press_down_arrow(*args, **kwargs)

    def 左矢印を押します(self, *args, **kwargs):
        # press_left_arrow(selector="html", times=1)
        return self.press_left_arrow(*args, **kwargs)

    def 右矢印を押します(self, *args, **kwargs):
        # press_right_arrow(selector="html", times=1)
        return self.press_right_arrow(*args, **kwargs)

    def 表示要素をクリックします(self, *args, **kwargs):
        # click_visible_elements(selector)
        return self.click_visible_elements(*args, **kwargs)

    def テキストでオプションを選択(self, *args, **kwargs):
        # select_option_by_text(dropdown_selector, option)
        return self.select_option_by_text(*args, **kwargs)

    def インデックスでオプションを選択(self, *args, **kwargs):
        # select_option_by_index(dropdown_selector, option)
        return self.select_option_by_index(*args, **kwargs)

    def 値でオプションを選択(self, *args, **kwargs):
        # select_option_by_value(dropdown_selector, option)
        return self.select_option_by_value(*args, **kwargs)

    def プレゼンテーションを作成する(self, *args, **kwargs):
        # create_presentation(name=None, theme="default")
        return self.create_presentation(*args, **kwargs)

    def スライドを追加する(self, *args, **kwargs):
        # add_slide(content=None, image=None, code=None, iframe=None,
        #           content2=None, notes=None, name=None)
        return self.add_slide(*args, **kwargs)

    def プレゼンテーションを保存する(self, *args, **kwargs):
        # save_presentation(name=None, filename=None,
        #                   show_notes=True, interval=0)
        return self.save_presentation(*args, **kwargs)

    def プレゼンテーションを開始する(self, *args, **kwargs):
        # begin_presentation(name=None, filename=None,
        #                    show_notes=True, interval=0)
        return self.begin_presentation(*args, **kwargs)

    def ツアーを作成する(self, *args, **kwargs):
        # create_tour(name=None, theme=None)
        return self.create_tour(*args, **kwargs)

    def SHEPHERDツアーを作成する(self, *args, **kwargs):
        # create_shepherd_tour(name=None, theme=None)
        return self.create_shepherd_tour(*args, **kwargs)

    def BOOTSTRAPツアーを作成する(self, *args, **kwargs):
        # create_bootstrap_tour(name=None, theme=None)
        return self.create_bootstrap_tour(*args, **kwargs)

    def DRIVERJSツアーを作成する(self, *args, **kwargs):
        # create_driverjs_tour(name=None, theme=None)
        return self.create_driverjs_tour(*args, **kwargs)

    def HOPSCOTCHツアーを作成する(self, *args, **kwargs):
        # create_hopscotch_tour(name=None, theme=None)
        return self.create_hopscotch_tour(*args, **kwargs)

    def INTROJSツアーを作成する(self, *args, **kwargs):
        # create_introjs_tour(name=None, theme=None)
        return self.create_introjs_tour(*args, **kwargs)

    def ツアーステップを追加する(self, *args, **kwargs):
        # add_tour_step(message, selector=None, name=None,
        #               title=None, theme=None, alignment=None)
        return self.add_tour_step(*args, **kwargs)

    def ツアーを再生する(self, *args, **kwargs):
        # play_tour(name=None)
        return self.play_tour(*args, **kwargs)

    def ツアーをエクスポートする(self, *args, **kwargs):
        # export_tour(name=None, filename="my_tour.js", url=None)
        return self.export_tour(*args, **kwargs)

    def 失敗(self, *args, **kwargs):
        # fail(msg=None)  # Inherited from "unittest"
        return self.fail(*args, **kwargs)

    def を取得する(self, *args, **kwargs):
        # get(url)  # Same as open(url)
        return self.get(*args, **kwargs)

    def を訪問(self, *args, **kwargs):
        # visit(url)  # Same as open(url)
        return self.visit(*args, **kwargs)

    def URLを訪問(self, *args, **kwargs):
        # visit_url(url)  # Same as open(url)
        return self.visit_url(*args, **kwargs)

    def 要素を取得する(self, *args, **kwargs):
        # get_element(selector)  # Element can be hidden
        return self.get_element(*args, **kwargs)

    def 要素を見つける(self, *args, **kwargs):
        # find_element(selector)  # Element must be visible
        return self.find_element(*args, **kwargs)

    def テキストを見つける(self, *args, **kwargs):
        # find_text(text, selector="html")  # Same as wait_for_text
        return self.find_text(*args, **kwargs)

    def 属性を取得する(self, *args, **kwargs):
        # get_attribute(selector, attribute)
        return self.get_attribute(*args, **kwargs)

    def 属性を設定する(self, *args, **kwargs):
        # set_attribute(selector, attribute, value)
        return self.set_attribute(*args, **kwargs)

    def すべての属性を設定(self, *args, **kwargs):
        # set_attributes(selector, attribute, value)
        return self.set_attributes(*args, **kwargs)

    def 書く(self, *args, **kwargs):
        # write(selector, text)  # Same as update_text()
        return self.write(*args, **kwargs)

    def メッセージのスタイルを設定する(self, *args, **kwargs):
        # set_messenger_theme(theme="default", location="default")
        return self.set_messenger_theme(*args, **kwargs)

    def メッセージを表示する(self, *args, **kwargs):
        # post_message(message, duration=None, pause=True, style="info")
        return self.post_message(*args, **kwargs)

    def 印刷(self, *args, **kwargs):
        # _print(msg)  # Same as Python print()
        return self._print(*args, **kwargs)

    def を延期する要素を確認する(self, *args, **kwargs):
        # deferred_assert_element(selector)
        return self.deferred_assert_element(*args, **kwargs)

    def を延期するテキストを確認する(self, *args, **kwargs):
        # deferred_assert_text(text, selector="html")
        return self.deferred_assert_text(*args, **kwargs)

    def 遅延アサーションの処理(self, *args, **kwargs):
        # process_deferred_asserts(print_only=False)
        return self.process_deferred_asserts(*args, **kwargs)

    def アラートを受け入れる(self, *args, **kwargs):
        # accept_alert(timeout=None)
        return self.accept_alert(*args, **kwargs)

    def アラートを却下(self, *args, **kwargs):
        # dismiss_alert(timeout=None)
        return self.dismiss_alert(*args, **kwargs)

    def アラートに切り替え(self, *args, **kwargs):
        # switch_to_alert(timeout=None)
        return self.switch_to_alert(*args, **kwargs)

    def HTMLファイルを読み込む(self, *args, **kwargs):
        # load_html_file(html_file, new_page=True)
        return self.load_html_file(*args, **kwargs)

    def HTMLファイルを開く(self, *args, **kwargs):
        # open_html_file(html_file)
        return self.open_html_file(*args, **kwargs)

    def ユーザーエージェントの取得(self, *args, **kwargs):
        # get_user_agent()
        return self.get_user_agent(*args, **kwargs)


class MasterQA_日本語(MasterQA, セレニウムテストケース):

    def を確認する(self, *args, **kwargs):
        # "Manual Check"
        self.DEFAULT_VALIDATION_TITLE = "手動チェック"
        # "Does the page look good?"
        self.DEFAULT_VALIDATION_MESSAGE = "ページは見栄えが良いですか?"
        # verify(QUESTION)
        return self.verify(*args, **kwargs)
