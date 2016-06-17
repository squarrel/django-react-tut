var CommentBox = React.createClass({
	render: function() {
		render (
			<div className="commentBox">
				<h3>Comments</h3>
				<CommentList />
				<CommentForm />
			</div>
		);
	});
	ReactDOM.render(
		<CommentBox />,
		document.getElementById('content')
	);

var CommentList = React.createClass({
	render: function() {
		return (
			<div className="commentList">
				Hello, world! I am a CommentList.
			</div>
		);
	}
});

var CommentForm = React.createClass({
	render: function() {
		return (
			<div className="commentForm">
				Hello, world! I am a CommentForm.
			</div>
		);
	}
});
