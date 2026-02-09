## 프로젝트 목록

### 1. 날씨 정보 앱 (Weather App)
- **파일**: `Weather_App.html`, `Weather_App.js`, `Weather_App.css`
- **API**: OpenWeatherMap API
- **설명**: 도시 이름을 입력하여 실시간 날씨 정보를 확인할 수 있는 웹 애플리케이션

### 2. 영화 검색 앱 (Movie Search App)
- **파일**: `Movie_Search.html`, `Movie_Search.css`
- **API**: TMDB (The Movie Database) API
- **설명**: 영화 제목 검색과 인기 영화 목록을 제공하는 웹 애플리케이션


## 🌤️ 1. 날씨 정보 앱

### 기능 소개

#### 주요 기능
1. **도시 검색**: 전 세계 도시 이름을 입력하여 날씨 정보 조회
2. **실시간 날씨 정보**: 현재 온도, 날씨 상태, 날씨 아이콘 표시
3. **상세 정보**: 체감 온도, 습도, 풍속, 기압 등 상세 날씨 데이터
4. **사용자 친화적 UI**: 로딩 표시, 에러 메시지, 반응형 디자인
5. **키보드 지원**: Enter 키로 검색 가능

#### 기술 스택
- **HTML5**: 시맨틱 마크업
- **CSS3**: Flexbox, Grid, 그라디언트, 애니메이션
- **JavaScript (ES6+)**: async/await, Fetch API, DOM 조작
- **API**: OpenWeatherMap Weather API

### 파일 구조

```
Weather_App.html    - HTML 구조
Weather_App.js      - JavaScript 로직
Weather_App.css     - 스타일시트
```

### 주요 코드 설명

#### 1. API 호출 (Weather_App.js)

```javascript
async function getWeather(city) {
  try {
    // 로딩 상태 표시
    showLoading();
    hideError();
    hideWeatherInfo();

    // OpenWeatherMap API 호출
    // units=metric: 섭씨 온도 사용
    // lang=kr: 한국어 날씨 설명
    const response = await fetch(
      `${BASE_URL}?q=${city}&appid=${API_KEY}&units=metric&lang=kr`
    );

    // HTTP 응답 상태 확인
    if (!response.ok) {
      if (response.status === 404) {
        throw new Error("도시를 찾을 수 없습니다.");
      }
      throw new Error("날씨 정보를 가져오는데 실패했습니다.");
    }

    // JSON 데이터 파싱
    const weather = await response.json();

    // 화면에 날씨 정보 표시
    displayWeather(weather);

    return weather;
  } catch (err) {
    // 에러 처리
    showError(err.message);
  } finally {
    // 로딩 상태 해제
    hideLoading();
  }
}
```

**핵심 학습 포인트:**
- `async/await`: 비동기 함수를 동기적으로 작성
- `try-catch-finally`: 에러 처리 및 정리 작업
- `response.ok`: HTTP 응답 상태 확인 (200-299)
- 쿼리 파라미터: `q`, `appid`, `units`, `lang`

#### 2. 데이터 표시 (Weather_App.js)

```javascript
function displayWeather(data) {
  // 도시 및 국가 정보
  cityName.textContent = data.name;
  countryName.textContent = data.sys.country;

  // 날씨 아이콘 설정
  const iconCode = data.weather[0].icon;
  weatherIcon.src = `https://openweathermap.org/img/wn/${iconCode}@2x.png`;

  // 온도 (소수점 첫째 자리까지)
  temp.textContent = Math.round(data.main.temp * 10) / 10;

  // 날씨 설명 (예: "맑음", "흐림")
  weatherDesc.textContent = data.weather[0].description;

  // 상세 정보
  feelsLike.textContent = Math.round(data.main.feels_like * 10) / 10;
  humidity.textContent = data.main.humidity;
  windSpeed.textContent = Math.round(data.wind.speed * 10) / 10;
  pressure.textContent = data.main.pressure;

  // 날씨 정보 영역 표시
  showWeatherInfo();
}
```

**핵심 학습 포인트:**
- **API 응답 데이터 구조 이해**:
  - `data.name`: 도시 이름
  - `data.sys.country`: 국가 코드
  - `data.weather[0].icon`: 날씨 아이콘 코드
  - `data.main.temp`: 현재 온도
  - `data.main.feels_like`: 체감 온도
  - `data.main.humidity`: 습도
  - `data.wind.speed`: 풍속
  - `data.main.pressure`: 기압
- **textContent**: 텍스트 안전하게 삽입 (XSS 방지)
- **Math.round()**: 반올림을 통한 소수점 제어

#### 3. 이벤트 리스너 (Weather_App.js)

```javascript
// 검색 버튼 클릭 이벤트
searchBtn.addEventListener("click", handleSearch);

// Enter 키로 검색 가능
cityInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    handleSearch();
  }
});

// 페이지 로드 시 서울 날씨를 기본으로 표시
window.addEventListener("DOMContentLoaded", () => {
  getWeather("Seoul");
});
```

**핵심 학습 포인트:**
- `addEventListener`: 이벤트 리스너 등록
- `keypress` 이벤트: 키보드 입력 감지
- `DOMContentLoaded`: DOM 트리 완성 후 실행

### 실행 방법

1. `Weather_App.html` 파일을 브라우저에서 엽니다
2. 도시 이름을 입력합니다 (예: Seoul, Tokyo, New York)
3. "검색" 버튼을 클릭하거나 Enter 키를 누릅니다
4. 날씨 정보가 표시됩니다

### API 정보

- **API 제공자**: OpenWeatherMap
- **API 문서**: https://openweathermap.org/api
- **사용 API**: Current Weather Data
- **엔드포인트**: `https://api.openweathermap.org/data/2.5/weather`

---

## 🎬 2. 영화 검색 앱

### 기능 소개

#### 주요 기능
1. **영화 검색**: 영화 제목으로 검색
2. **인기 영화 목록**: 현재 인기 영화 목록 표시
3. **페이지네이션**: 이전/다음 페이지 이동 기능
4. **영화 상세 정보**: 클릭 시 모달로 상세 정보 표시
5. **포스터 및 배경 이미지**: 고화질 이미지 표시
6. **반응형 디자인**: 모바일, 태블릿, 데스크톱 지원

#### 기술 스택
- **HTML5**: 시맨틱 마크업, 모달 구조
- **CSS3**: Grid, Flexbox, 애니메이션, Netflix 스타일 디자인
- **JavaScript (ES6+)**: async/await, Fetch API, 템플릿 리터럴
- **API**: TMDB (The Movie Database) API

### 파일 구조

```
Movie_Search.html   - HTML 구조 및 JavaScript
Movie_Search.css    - 스타일시트
```

### 주요 코드 설명

#### 1. 이미지 URL 생성 (Movie_Search.html)

```javascript
/**
 * TMDB 이미지 URL 생성 함수
 * @param {string} path - 이미지 경로 (예: "/abc123.jpg")
 * @param {string} size - 이미지 크기 (w500, original 등)
 * @returns {string} 완성된 이미지 URL
 */
function getImageUrl(path, size = "w500") {
  // path가 없으면 placeholder 이미지 반환
  return path
    ? `${IMG_BASE}/${size}${path}`
    : "https://via.placeholder.com/500x750?text=No+Image";
}

// 사용 예시
// 포스터: getImageUrl(movie.poster_path, "w500")
// 배경: getImageUrl(movie.backdrop_path, "original")
```

**핵심 학습 포인트:**
- **템플릿 리터럴**: 문자열 조합을 깔끔하게 작성
- **삼항 연산자**: 조건부 반환값
- **기본 매개변수**: `size = "w500"`로 기본값 설정
- **TMDB 이미지 크기**:
  - `w500`: 포스터용 (500px 너비)
  - `original`: 배경용 (원본 크기)

#### 2. 인기 영화 목록 조회 (Movie_Search.html)

```javascript
/**
 * 인기 영화 목록을 가져오는 함수
 * @param {number} page - 페이지 번호
 */
async function getPopularMovies(page = 1) {
  try {
    // API 호출
    const response = await fetch(
      `${BASE_URL}/movie/popular?api_key=${API_KEY}&language=ko-KR&page=${page}`
    );

    // 응답 상태 확인
    if (!response.ok) {
      throw new Error("영화 정보를 가져오는데 실패했습니다.");
    }

    // JSON 데이터 파싱
    const data = await response.json();
    console.log(`인기 영화 (페이지 ${page}):`, data);

    // 영화 목록 표시
    displayMovies(data.results, popularMovieList);

    // 페이지 정보 업데이트
    currentPage = page;
    updatePagination(data.page, data.total_pages);

    return data;
  } catch (error) {
    console.error("인기 영화 조회 오류:", error);
    showMessage("인기 영화를 불러오는데 실패했습니다.", "error");
  }
}
```

**핵심 학습 포인트:**
- **API 쿼리 파라미터**:
  - `api_key`: API 인증 키
  - `language=ko-KR`: 한국어 데이터
  - `page`: 페이지 번호 (페이지네이션)
- **응답 데이터 구조**:
  - `data.results`: 영화 배열
  - `data.page`: 현재 페이지
  - `data.total_pages`: 전체 페이지 수

#### 3. 영화 검색 (Movie_Search.html)

```javascript
/**
 * 영화를 검색하는 함수
 * @param {string} query - 검색어
 */
async function searchMovies(query) {
  try {
    hideMessage();

    // 검색 API 호출
    const response = await fetch(
      `${BASE_URL}/search/movie?api_key=${API_KEY}&language=ko-KR&query=${encodeURIComponent(query)}`
    );

    if (!response.ok) {
      throw new Error("영화 검색에 실패했습니다.");
    }

    const data = await response.json();

    // 검색 결과가 없는 경우
    if (data.results.length === 0) {
      showMessage("검색 결과가 없습니다.", "info");
      hideSearchResults();
      return;
    }

    // 검색 결과 표시
    displayMovies(data.results, searchMovieList);
    showSearchResults();
    hidePopularMovies();

    return data;
  } catch (error) {
    console.error("영화 검색 오류:", error);
    showMessage("영화 검색에 실패했습니다.", "error");
  }
}
```

**핵심 학습 포인트:**
- `encodeURIComponent()`: URL 안전한 문자열로 인코딩
  - 예: "Avengers: Endgame" → "Avengers%3A%20Endgame"
- **조건부 UI 표시**: 검색 결과 유무에 따라 다른 UI 표시
- **API 엔드포인트 차이**:
  - 인기 영화: `/movie/popular`
  - 검색: `/search/movie`

#### 4. 영화 목록 표시 (Movie_Search.html)

```javascript
/**
 * 영화 목록을 화면에 표시하는 함수
 * @param {Array} movies - 영화 배열
 * @param {HTMLElement} container - 영화를 표시할 컨테이너
 */
function displayMovies(movies, container) {
  container.innerHTML = movies
    .map(
      (movie) => `
      <div class="movie-card" onclick="getMovieDetails(${movie.id})">
        <img src="${getImageUrl(movie.poster_path)}" alt="${movie.title}" />
        <div class="movie-info">
          <h3 class="movie-title">${movie.title}</h3>
          <div class="movie-meta">
            <span class="rating">⭐ ${movie.vote_average.toFixed(1)}</span>
            <span class="release-date">${movie.release_date || "미정"}</span>
          </div>
        </div>
      </div>
    `
    )
    .join("");
}
```

**핵심 학습 포인트:**
- **배열 메소드 체이닝**:
  - `map()`: 배열을 HTML 문자열 배열로 변환
  - `join("")`: 배열을 하나의 문자열로 결합
- **템플릿 리터럴**: 동적 HTML 생성
- **인라인 이벤트 핸들러**: `onclick="getMovieDetails(${movie.id})"`
- **널 병합**: `movie.release_date || "미정"` (개봉일이 없으면 "미정" 표시)
- **toFixed()**: 소수점 자릿수 고정 (평점 표시)

#### 5. 영화 상세 정보 표시 (Movie_Search.html)

```javascript
/**
 * 영화 상세 정보를 가져오는 함수
 * @param {number} movieId - 영화 ID
 */
async function getMovieDetails(movieId) {
  try {
    // 상세 정보 API 호출
    const response = await fetch(
      `${BASE_URL}/movie/${movieId}?api_key=${API_KEY}&language=ko-KR`
    );

    if (!response.ok) {
      throw new Error("영화 상세 정보를 가져오는데 실패했습니다.");
    }

    const movie = await response.json();
    console.log("영화 상세 정보:", movie);

    // 모달에 상세 정보 표시
    displayMovieDetails(movie);

    return movie;
  } catch (error) {
    console.error("영화 상세 정보 조회 오류:", error);
    alert("영화 상세 정보를 불러오는데 실패했습니다.");
  }
}

/**
 * 영화 상세 정보를 모달에 표시
 */
function displayMovieDetails(movie) {
  modalBody.innerHTML = `
    <div class="movie-detail">
      ${
        movie.backdrop_path
          ? `<div class="backdrop" style="background-image: url('${getImageUrl(movie.backdrop_path, "original")}')"></div>`
          : ""
      }
      <div class="detail-content">
        <div class="detail-main">
          <img class="detail-poster" src="${getImageUrl(movie.poster_path)}" />
          <div class="detail-info">
            <h2>${movie.title}</h2>
            ${movie.original_title !== movie.title ? `<p class="original-title">${movie.original_title}</p>` : ""}
            <div class="detail-meta">
              <span class="rating">⭐ ${movie.vote_average.toFixed(1)}</span>
              <span>${movie.release_date || "미정"}</span>
              <span>${movie.runtime ? `${movie.runtime}분` : ""}</span>
            </div>
            <div class="genres">
              ${movie.genres.map((genre) => `<span class="genre-tag">${genre.name}</span>`).join("")}
            </div>
            <div class="overview">
              <h3>줄거리</h3>
              <p>${movie.overview || "줄거리 정보가 없습니다."}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;

  // 모달 표시
  modal.style.display = "flex";
}
```

**핵심 학습 포인트:**
- **REST API 패턴**: `/movie/{id}` - 특정 영화 상세 정보
- **조건부 렌더링**:
  - 배경 이미지가 있을 때만 표시
  - 원제와 다를 때만 원제 표시
  - 런타임이 있을 때만 표시
- **배열 변환**: `movie.genres.map()` - 장르 배열을 HTML로 변환
- **모달 표시**: `modal.style.display = "flex"`

#### 6. 페이지네이션 (Movie_Search.html)

```javascript
/**
 * 페이지네이션 버튼 상태 업데이트
 */
function updatePagination(page, totalPages) {
  pageInfo.textContent = `페이지 ${page}`;
  prevBtn.disabled = page <= 1;          // 첫 페이지면 이전 버튼 비활성화
  nextBtn.disabled = page >= totalPages; // 마지막 페이지면 다음 버튼 비활성화
}

// 이전 페이지 버튼
prevBtn.addEventListener("click", () => {
  if (currentPage > 1) {
    getPopularMovies(currentPage - 1);
  }
});

// 다음 페이지 버튼
nextBtn.addEventListener("click", () => {
  getPopularMovies(currentPage + 1);
});
```

**핵심 학습 포인트:**
- **버튼 상태 제어**: `disabled` 속성으로 비활성화
- **페이지 상태 관리**: `currentPage` 전역 변수로 현재 페이지 추적
- **조건부 API 호출**: 페이지 범위 확인 후 API 호출

#### 7. 모달 제어 (Movie_Search.html)

```javascript
// 모달 닫기 버튼
closeModal.addEventListener("click", () => {
  modal.style.display = "none";
});

// 모달 바깥 클릭 시 닫기
modal.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.style.display = "none";
  }
});

// ESC 키로 모달 닫기
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && modal.style.display === "flex") {
    modal.style.display = "none";
  }
});
```

**핵심 학습 포인트:**
- **이벤트 타겟 확인**: `e.target === modal` - 모달 배경 클릭 감지
- **키보드 이벤트**: `keydown` 이벤트로 ESC 키 감지
- **UX 향상**: 다양한 방법으로 모달 닫기 (버튼, 배경, ESC 키)

### 실행 방법

1. `Movie_Search.html` 파일을 브라우저에서 엽니다
2. 페이지가 로드되면 자동으로 인기 영화 목록이 표시됩니다
3. 검색창에 영화 제목을 입력하여 검색할 수 있습니다
4. 영화 카드를 클릭하면 상세 정보가 모달로 표시됩니다
5. 페이지 하단의 "이전/다음" 버튼으로 다른 페이지를 탐색할 수 있습니다

### API 정보

- **API 제공자**: TMDB (The Movie Database)
- **API 문서**: https://developers.themoviedb.org/3
- **사용 API**:
  - Popular Movies: `/movie/popular`
  - Search Movies: `/search/movie`
  - Movie Details: `/movie/{id}`
- **이미지 베이스 URL**: `https://image.tmdb.org/t/p`

---

## 💡 학습 포인트

### 공통 학습 내용

#### 1. Fetch API
```javascript
// 기본 사용법
const response = await fetch(url);
const data = await response.json();

// 응답 상태 확인
if (!response.ok) {
  throw new Error("API 호출 실패");
}
```

#### 2. async/await
```javascript
// async 함수 선언
async function getData() {
  try {
    const response = await fetch(url);  // 비동기 작업 대기
    const data = await response.json(); // JSON 파싱 대기
    return data;
  } catch (error) {
    console.error(error);
  }
}
```

#### 3. try-catch-finally
```javascript
try {
  // 실행할 코드
  const data = await fetch(url);
} catch (error) {
  // 에러 처리
  console.error(error);
} finally {
  // 항상 실행되는 코드 (정리 작업)
  hideLoading();
}
```

#### 4. DOM 조작
```javascript
// 요소 선택
const element = document.getElementById("id");

// 텍스트 변경
element.textContent = "새 텍스트";

// HTML 변경
element.innerHTML = "<p>새 HTML</p>";

// 스타일 변경
element.style.display = "block";

// 클래스 추가/제거
element.classList.add("active");
element.classList.remove("hidden");
```

#### 5. 이벤트 처리
```javascript
// 클릭 이벤트
button.addEventListener("click", handleClick);

// 키보드 이벤트
input.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    handleSearch();
  }
});

// 페이지 로드 이벤트
window.addEventListener("DOMContentLoaded", init);
```

### 날씨 앱 특화 학습

1. **API 쿼리 파라미터 활용**
   - `units=metric`: 온도 단위 설정
   - `lang=kr`: 응답 언어 설정

2. **에러 처리**
   - HTTP 상태 코드 확인 (404, 500 등)
   - 사용자 친화적인 에러 메시지 표시

3. **UI/UX**
   - 로딩 상태 표시
   - 기본 도시 설정 (Seoul)

### 영화 앱 특화 학습

1. **페이지네이션**
   - 페이지 번호로 데이터 분할 조회
   - 이전/다음 버튼 상태 관리

2. **모달 구현**
   - 동적 콘텐츠 삽입
   - 다양한 닫기 방법 (버튼, 배경, ESC)

3. **이미지 처리**
   - 다양한 이미지 크기 활용
   - 이미지 없을 때 placeholder 표시

4. **복잡한 UI 상태 관리**
   - 검색 결과와 인기 영화 목록 전환
   - 조건부 UI 표시/숨김

---

## 📝 참고 자료

### API 문서
- [OpenWeatherMap API](https://openweathermap.org/api)
- [TMDB API](https://developers.themoviedb.org/3)

### MDN 문서
- [Fetch API](https://developer.mozilla.org/ko/docs/Web/API/Fetch_API)
- [async/await](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/async_function)
- [Promise](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise)

---

## 📌 주의사항

### API 키 관리
- 현재 코드에는 API 키가 하드코딩되어 있음
- 실제 프로덕션 환경에서는 환경 변수나 서버 측에서 관리해야 함
- API 키를 GitHub 등에 공개하지 않도록 주의

### CORS 이슈
- 두 API 모두 CORS를 허용하므로 클라이언트에서 직접 호출 가능
- 다른 API를 사용할 때는 CORS 정책을 확인

### API 사용 제한
- 무료 API는 요청 횟수 제한이 있을 수 있음
- 과도한 요청을 피하고 필요할 때만 API를 호출
