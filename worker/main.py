import re
import httpx


def main_get_github_v2(query: str) -> str:
    owner = "langgenius"
    repo = "dify"
    g_number = get_github_number(query)
    lite_prompt = "<Guide>This is a GitHub issue or pull request detail that containing title, state, creation date, body, and possibly comments; analyze all elements thoroughly, focusing on problem description, technical details, reproduction steps, error messages, and any new information or solutions in comments.</Guide>"
    base_url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Accept": "application/vnd.github.v3+json"}

    with httpx.Client() as client:
        # Fetch issue
        issue_response = client.get(
            f"{base_url}/issues/{g_number}", headers=headers)
        if issue_response.status_code != 200:
            return f"Error: {issue_response.status_code}"

        issue = issue_response.json()

        # Fetch comments
        comments_response = client.get(
            f"{base_url}/issues/{g_number}/comments", headers=headers
        )
        comments = []
        if comments_response.status_code == 200:
            comments = [comment["body"]
                        for comment in comments_response.json()]

    # Format comments using the new function
    comments_str = format_comments(comments)

    # Create the single-line string output
    result = f"<GitHub issue>{lite_prompt}<title>{issue['title']}</title><state>{issue['state']}</state><created_at>{issue['created_at']}</created_at><body>{issue['body']}</body>{comments_str}</GitHub issue>"

    return {
        "result": result,
        "url": f"https://github.com/{owner}/{repo}/issues/{g_number}",
    }


def main_get_github(query: str) -> str:
    owner = "langgenius"
    repo = "dify"
    g_number = get_github_number(query)
    lite_prompt = "<Guide>This is a GitHub issue or pull request detail that containing title, state, creation date, body, and possibly comments.</Guide>"
    base_url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Accept": "application/vnd.github.v3+json"}

    with httpx.Client() as client:
        # Fetch issue
        issue_response = client.get(
            f"{base_url}/issues/{g_number}", headers=headers)
        if issue_response.status_code != 200:
            return {
                "result": f"Error: {issue_response.status_code}",
                "url": f"https://github.com/{owner}/{repo}/issues/{g_number}",
            }

        issue = issue_response.json()

        # Fetch comments
        comments_response = client.get(
            f"{base_url}/issues/{g_number}/comments", headers=headers
        )
        comments = []
        if comments_response.status_code == 200:
            comments = [comment["body"]
                        for comment in comments_response.json()]

    # Format comments using the new function
    comments_str = format_comments(comments)

    # Create the single-line string output
    content = f"<GitHub issue>{lite_prompt}<title>{issue['title']}</title><state>{issue['state']}</state><created_at>{issue['created_at']}</created_at><body>{issue['body']}</body>{comments_str}</GitHub issue>"

    return {"content": content}


def 检查是否收集过(raw_source: str, api_key: str, api_url: str) -> dict:
    space_index = raw_source.find(" ")

    if space_index == -1:
        source = raw_source
    else:
        source = raw_source[:space_index]

    url = f"{api_url}/api/feature_raw/init?url={source}"

    headers = {
        "accept": "*/*",
        "Authorization": f"Bearer {api_key}"
    }

    with httpx.Client() as client:
        response = client.get(url, headers=headers)

    return {
        "status_code": response.status_code,
        "response_text": response.text,
        "source": source
    }


def 解析并发表评论(
    comment: str, user: str, f_id: int, api_key: str, api_url: str
) -> dict:
    import time

    comment = f"<comment user='{user}' time='{time.strftime('%Y-%m-%d %H:%M:%S')}'>{comment[9:]}</comment>"
    url = f"{api_url}/api/feature_raw_add_comment"
    headers = {"Authorization": f"Bearer {api_key}"}

    params = {"feature_id": int(f_id), "comment": comment}

    with httpx.Client() as client:
        response = client.post(url, params=params, headers=headers)

    return {"status_code": response.status_code, "response_text": response.text}


"""
Input Variables:
input_string: String
Output Variables:
content_inside: String, content_outside: String
"""


def 解析包含的原始内容(input_string: str) -> dict:
    pattern = r'<content>(.*?)</content>'
    match = re.search(pattern, input_string, re.DOTALL)

    if match:
        content_inside = match.group(1)
        content_outside = re.sub(pattern, '', input_string, flags=re.DOTALL)
    else:
        content_inside = ""
        content_outside = input_string

    return {
        "content": content_inside,
        "comment": content_outside
    }


def get_github_number(url: str):
    start = url.rfind("/")
    if start == -1:
        return {"number": 0}

    number = ""
    for char in url[start + 1:]:
        if char.isdigit():
            number += char
        else:
            break
    return number


def format_comments(comments):
    formatted_comments = ""
    for comment in comments:
        if "<!-- Greeting -->" in comment:
            formatted_comments += f"<bot_comment>{comment}</bot_comment>"
        else:
            formatted_comments += f"<comment>{comment}</comment>"
    return f"<comments>{formatted_comments}</comments>" if formatted_comments else ""


def GitHub解析器(query: str) -> str:
    owner = "langgenius"
    repo = "dify"
    g_number = get_github_number(query)
    lite_prompt = "<Guide>This is a GitHub issue or pull request detail that containing title, state, creation date, body, and possibly comments.</Guide>"
    base_url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Accept": "application/vnd.github.v3+json"}

    with httpx.Client() as client:
        # Fetch issue
        issue_response = client.get(
            f"{base_url}/issues/{g_number}", headers=headers
        )
        if issue_response.status_code != 200:
            return {
                "result": f"Error: {issue_response.status_code}",
                "url": f"https://github.com/{owner}/{repo}/issues/{g_number}",
            }

        issue = issue_response.json()

        # Fetch comments
        comments_response = client.get(
            f"{base_url}/issues/{g_number}/comments", headers=headers
        )
        comments = []
        if comments_response.status_code == 200:
            comments = [comment["body"]
                        for comment in comments_response.json()]

    # Format comments using the new function
    comments_str = format_comments(comments)

    # Create the single-line string output
    content = f"<GitHub issue>{lite_prompt}<title>{issue['title']}</title><state>{issue['state']}</state><created_at>{issue['created_at']}</created_at><body>{issue['body']}</body>{comments_str}</GitHub issue>"

    return {"content": content}


def store_feature_request_raw(
        content: str, summary: str, source: str, api_key: str, api_url: str) -> dict:
    url = f"{api_url}/api/feature_raw"

    payload = {"content": content, "summary": summary, "source": source}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    with httpx.Client() as client:
        response = client.put(url, json=payload, headers=headers)

    return {
        "status_code": response.status_code,
        "response_text": int(response.text),
    }
